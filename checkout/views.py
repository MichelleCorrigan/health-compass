from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('programmes'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NLqkIIoTYTzAxck2JIaKINue90HfJe9wQU9rvW0cWOaCFOoqQYLmaSWAMYWuT5TWdNfkcJOrmbNu1pXqRMLtAgs00bY5xxwPA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
