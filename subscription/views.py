from django.shortcuts import render, redirect
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
            return redirect('home')

    form = SubscriptionForm

    context = {
        'form': form,
    }

    template = 'subscription/subscription.html'

    return render(request, template, context)
