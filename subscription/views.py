from django.shortcuts import render
from django.contrib import messages

from .forms import SubscriptionForm


def subscription_list(request):
    """
    Customers can subscribe to our website
    """
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Thank you for subscribing!')

    form = SubscriptionForm

    context = {
        'form': form,
    }

    template = 'subscription/subscription_list.html'

    return render(request, template, context)
