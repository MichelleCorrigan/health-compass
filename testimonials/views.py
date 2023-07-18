from django.shortcuts import render
from .models import Testimonial

# Create your views here.


def testimonials(request):
    """ A view to return the testimonials page """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)
