from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Genre


def all_books(request):
    """A view to return all books, including searhcing and sorting the books"""

    books = Book.objects.all()
    query = None
    genres = None

    if request.GET:
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

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
    }
    
    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ A view to return individual book details """ 

    book = get_object_or_404(Book, pk=book_id)

    context = {
    'book': book,
    }

    return render(request, 'books/book_detail.html', context)