from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Author
from .forms import AuthorForm

def author_bio(request, author_id):
    """ A view to disply individual author details """

    author = get_object_or_404(Author, id=author_id)

    context = {
        'author': author,
    }
    
    return render(request, 'author/author_bio.html', context)


@login_required
def add_author(request):
    """ Add an author to the database"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    if request.Method == 'POST':
        form = AuthorForm(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Author.')
            return redirect(reverse('add_author'))
        else:
            messages.error(request, 'Failed to add Author. Please ensure form is valid.')
    else:
        form = AuthorForm()

    template = 'authors/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_author(request, author_id):
    """ Edit an author in the database"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only book shop owners can do that.')
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=author_id, instane=author)
    if request.Method == 'POST':
        form = AuthorForm(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Author.')
            return redirect(reverse('author_bio', args=[author_id]))
        else:
            messages.error(request, 'Failed to update Author. Please ensure form is valid.')
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
    """ Delete an author fro0m the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, onluy book shop oweners can do that.')
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    messages.success(request, 'Author deleted!')
    return redirect(reverse('books'))