from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Author
from .forms import AuthorForm

"""
views.py for authors app
"""


def authors(request):
    """ A view to display a list of authors sorted by surname """
    

    authors = Author.objects.all()
    
    sorted_authors = sorted(authors, key=lambda author: author.name.split()[-1].lower())
    
    context = {
        'authors': sorted_authors
    }
    
    return render(request, 'authors/authors.html', context)


def author_bio(request, author_id):
    """ A view to disply individual author details """

    author = get_object_or_404(Author, id=author_id)

    context = {
        'author': author,
    }

    return render(request, 'authors/author_bio.html', context)


@login_required
def add_author(request):
    """ Add an author to the database"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            messages.success(request, f'Successfully added {author.name}.')
            return redirect(reverse('add_author'))
        else:
            messages.error
            (request, 'Failed to add Author. Please ensure form is valid.')
    else:
        form = AuthorForm()

    template = 'authors/add_author.html'
    context = {
        'form': form,
    }

    return redirect(reverse('authors'))


@login_required
def edit_author(request, author_id):
    """ Edit an author in the database"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=author_id,)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Author.')
            return redirect(reverse('author_bio', args=[author_id]))
        else:
            messages.error
            (request, 'Failed to update Author. Please ensure form is valid.')
    else:
        form = AuthorForm(instance=author)
        messages.info(request, f'You are editing {author.name}')

    template = 'authors/edit_author.html'
    context = {
        'form': form,
        'author': author
    }

    return render(request, template, context)


@login_required
def delete_author(request, author_id):
    """ Delete an author from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    messages.success(request, f'Author: {author.name} deleted!')
    
    return redirect(reverse('authors'))
    