from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book
import logging

def basket_contents(request):

    basket_items = []
    total = Decimal('0.00')
    book_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
  
        book = get_object_or_404(Book, pk=item_id)
        if book.offer:
            price = book.price * Decimal('0.90')
        else:
            price = book.price

        total += quantity * price
        book_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * (settings.STANDARD_DELIVERY_PERCENTAGE / Decimal('100.00'))
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
     
    total = total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    delivery = delivery.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    grand_total = (delivery + total).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    context = {
        'basket_items': basket_items,
        'total': f"{total:.2f}",
        'book_count': book_count,
        'delivery': f"{delivery:.2f}",
        'free_delivery_delta': f"{free_delivery_delta:.2f}",
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': f"{grand_total:.2f}",
    }

   # logger.debug(f"Basket Contents: {basket_items}") 
    # logger.debug(f"Total: {total}, FREE_DELIVERY_THRESHOLD: {settings.FREE_DELIVERY_THRESHOLD}, Free Delivery Delta: {free_delivery_delta}")
    return context



