from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from books.models import Book
# Create your views here.

def view_basket(request):
    """ A view to render the shopping basket page """
    ## context = basket_contents(request)
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified book to the shopping basket """

    book = Book.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {book.title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """ Adjusts the quantity of the specified book to the specified amount """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def update_quantity(request, item_id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id, None)

    request.session['basket'] = basket
    return redirect('view_basket')  


def remove_item(request, item_id):
    basket = request.session.get('basket', {})
    basket.pop(item_id, None)
    request.session['basket'] = basket
    return redirect('view_basket')

def my_view(request):
    basket_items = get_basket_items(request)
    print(f"Basket Items: {basket_items}")

    
    return render(request, 'basket.html', context={'basket_items': basket_items})


def remove_from_basket(request, item_id):
    """ Removes the item from the shopping basket """
    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)