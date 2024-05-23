from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout (request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket yet.")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PJhXlKRbG3iC6O6L1VbdhhJK73qzP7BwcxC3fI8m6mwIzlzxzam1HRPHQiwuTjbWq2hELXEciQa74OUILpoxXBN00OU4IYioN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)