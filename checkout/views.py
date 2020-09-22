from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the mement")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HUHJdBjaSvU6yf88OBQ\
            WOTgUft887PMgMCJP5E8y4PSMxqIduVBvYkbYkKlMjkQpJ8\
                dUg0KzyFcpClVhatbxeuJ00xXJYLl9h',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
