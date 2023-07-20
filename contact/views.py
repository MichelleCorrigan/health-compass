from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

# from .models import Testimonial
# from .forms import TestimonialForm


def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')
