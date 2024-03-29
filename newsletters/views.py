from django.shortcuts import render
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

# Create your views here.


def newsletters(request):
    """ A view to return the newsletter page """

    newsletters = NewsletterUser.objects.all()

    context = {
        'newsletters': newsletters,
    }

    return render(request, 'newsletters/newsletters.html', context)


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.error(request, 'This email has already signed up!')
        else:
            instance.save()
            messages.success(request, 'Thanks for signing up!')

    context = {
        'form': form,
    }
    template = 'newsletters/sign_up.html'
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'You have been unsubscribed.')
        else:
            messages.error(request, 'Sorry but we did not find your \
                email address')

    context = {
        'form': form,
    }

    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)
