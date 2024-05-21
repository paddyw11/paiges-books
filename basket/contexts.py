from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book
import logging

def basket_contents(request):

    basket_items = []
    total = 0
    book_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
  
        book = get_object_or_404(Book, pk=item_id)
        total += quantity * book.price
        book_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

   # logger.debug(f"Basket Contents: {basket_items}") 

    return context



