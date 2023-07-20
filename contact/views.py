from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Message Sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')

        send_mail(
            full_name,
            message,
            email,
            ['lal.corrigan@gmail.com',],
        )

        return render(request, 'contact/contact.html')

    else:
        return render(request, 'contact/contact.html')
