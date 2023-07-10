from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Contact_Form
from subscription.forms import SubscriptionForm


def contact(request):
    """
    Display a contact form and handle form submissions.
    """
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            contact_form = form.save(commit=False)
            if contact_form.newsletter:
                sub_form = SubscriptionForm(request.POST)
                sub_form.full_name = contact_form.full_name
                sub_form.email = contact_form.email
                sub_form.save()
            contact_form = form.save()
            messages.success(
                request,
                'Thank you for contacting Peak Nutrition!'
                ' We will be in touch soon.'
                )
            return redirect('home')
    else:
        form = Contact_Form()

    template = 'contact.html'
    context = {'form': form}
    return render(request, template, context)


def free_consult(request):
    """
    Display a custom free consultation contact form
    """
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            contact_form = form.save(commit=False)
            if contact_form.newsletter:
                sub_form = SubscriptionForm(request.POST)
                sub_form.full_name = contact_form.full_name
                sub_form.email = contact_form.email
                sub_form.save()
            contact_form = form.save()
            messages.success(
                request,
                'Thank you for requesting a FREE 15 minute\
                      consultation with Peak Nutrition!'
                ' We will be in touch soon to schedule.'
                )
            return redirect('home')
    else:
        form = Contact_Form(initial={
            'subject': 'I want to book my free 15 minute consultation',
            'message': 
            'Hi, I would like to book my free 15 minute consultation with you.'
            ' My preferred times are:',
            },
            )

    template = 'free_consult.html'
    context = {'form': form}
    return render(request, template, context)
