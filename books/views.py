from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F, Func, Value
from django.db.models.functions import Upper, Substr, Length, Lower
from django.core.paginator import Paginator
from .models import Book, Genre
from .forms import BookForm
from authors.models import Author


class Reverse(Func):
    function = 'REVERSE'


def all_books(request):
    """A view to return all books, including searching and sorting the books"""

    books = Book.objects.all()
    total_books = books.count()
    query = None
    genres = None
    sort = None
    direction = None
    is_wishlist = False

    print("GET parameters:", request.GET)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'author':

                books = books.annotate(
                    last_name=Substr(
                        F('author__name'),
                        Length(F('author__name')) - Func(Reverse(F(
                            'author__name')), Value(' '),
                            function='STRPOS') + 1,
                        Length(F('author__name'))
                    )
                )

                print("Extracted last name substring for sorting:")
                for book in books:
                    last_name_substr = book.last_name
                    print(f"Book: {book.title}, Last name used for sorting: \
                         {last_name_substr}")

                sortkey = 'last_name'

            elif sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('title'))

            print(f"Current sortkey: {sortkey}")

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

            print(f"Final sortkey with direction: {sortkey}")

        if 'genre' in request.GET:
            genre_name = request.GET['genre'].replace('_', ' ')
            genres = genre_name

            genre = Genre.objects.get(name=genre_name)
            
            books = books.filter(genres__name__iexact=genre_name)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | \
                Q(short_description__icontains=query) | \
                Q(author__name__icontains=query) | \
                Q(genres__name__icontains=query)
            books = books.filter(queries)

        if 'offer' in request.GET and request.GET['offer'] == 'true':
            books = books.filter(offer=True)
            print("Offer filter applied")

        if 'bookmark' in request.GET:
            books = books.filter(bookmark__id=request.user.id)
            is_wishlist = True

    filtered_books_count = books.count()

    paginator = Paginator(books, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
        'paginator': paginator,
        'page_obj': page_obj,
        'filtered_books_count': filtered_books_count,
        'total_books': total_books,
        'is_wishlist': is_wishlist
    }

    return render(request, 'books/books.html', context)


def books_on_offer(request):
    """ A view to display books that are on offer"""
    offer_books = Book.objects.filter(offer=True)

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                offer_books = offer_books.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            offer_books = offer_books.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'offer_books': offer_books,  
        'current_sorting': current_sorting
    }

    return render(request, 'books/offers.html', context)


def book_detail(request, book_id):
    """ A view to return individual book details """

    book = get_object_or_404(Book, pk=book_id)
    recommended_books = book.get_recommended_books()

    bookmark = False
    if book.bookmark.filter(id=request.user.id).exists():
        bookmark = True

    context = {
        'book': book,
        'recommended_books': recommended_books,
        'bookmark': bookmark,
    }

    return render(request, 'books/book_detail.html', context)


@login_required
def add_book(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to add book. \
            Please chck the form is valid.')
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """ Edit a book from the library """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to update book. \
            Please ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """ Delete a book from the library"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book successfully deleted!')
    return redirect(reverse('books'))


@login_required
def bookmark_add(request, book_id):
    """ A view to add/remove a book to a reading list """

    book = get_object_or_404(Book, pk=book_id)

    if book.bookmark.filter(id=request.user.id).exists():
        book.bookmark.remove(request.user)
    else:
        book.bookmark.add(request.user)

    return redirect('book_detail', book.id)
