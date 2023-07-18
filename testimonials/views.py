from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Testimonial

# Create your views here.


def testimonials(request):
    """ A view to return the testimonials page """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


@login_required
def delete_testimonial(request, testimonial_id):
    """ Delete a testimonial from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site administrators can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('testimonials'))