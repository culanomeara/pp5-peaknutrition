from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Display a contact form and handle form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for contacting Peak Nutrition!'
                ' We will be in touch soon.'
                )
            return redirect('home')
    else:
        form = ContactForm()

    template = 'contact.html'
    context = {'form': form}
    return render(request, template, context)


def free_consult(request):
    """
    Display a contact form and handle form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for requesting a FREE 15 minute consultation with Peak Nutrition!'
                ' We will be in touch soon to schedule.'
                )
            return redirect('home')
    else:
        form = ContactForm(initial={
            'subject': 'I want to book my free 15 minute consultation',
            'message': 'Hi, I would like to book my free 15 minute consultation with you. My preferred times are:',
            },
            )

    template = 'free_consult.html'
    context = {'form': form}
    return render(request, template, context)

    
