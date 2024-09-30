from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Genre
from .forms import BookForm


def all_books(request):
    """A view to return all books, including searhcing and sorting the books"""

    books = Book.objects.all()
    query = None
    genres = None
    sort = None
    direction = None
    

    print("GET parameters:", request.GET)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)


        if 'genre' in request.GET:
            genre_name = request.GET['genre'].replace('_', ' ')
            # genre_name = request.GET['genre']
            print("this  is genre name = ",genre_name)

            genre = Genre.objects.get(name=genre_name)
            print("this  is genre = ",genre)
            books = books.filter(genres__name__iexact=genre_name)
            
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(short_description__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

        if 'offer' in request.GET and request.GET['offer'] == 'true':
            books = books.filter(offer=True)
            print("Offer filter applied")

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
        
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
        'offer_books': offer_books,  # Only books with offers
        'current_sorting': current_sorting
    }
    
    return render(request, 'books/offers.html', context)

def book_detail(request, book_id):
    """ A view to return individual book details """ 

    book = get_object_or_404(Book, pk=book_id)
    recommended_books = book.get_recommended_books()

    context = {
    'book': book,
    'recommended_books': recommended_books,
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
            messages.error(request, 'Failed to add book. Please chck the form is valid.')
    else:
        form = BookForm()
        
    template = 'books/add_book.html'
    context = {
        'form' : form,
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
            messages.error(request, 'Failed to update book. Please ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')
   
    template = 'books/edit_book.html'
    context = {
        'form' : form,
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