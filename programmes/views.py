from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Programme
from .forms import ProgrammeForm


def all_programmes(request):
    """ A view to show individual programme details """

    programmes = Programme.objects.all()

    context = {
        'programmes': programmes,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_detail(request, programme_id):
    """ A view to show all programmes """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'programmes/programme_detail.html', context)


def add_programme(request):
    """ Add a programme to the site """
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added programme/service!')
            return redirect(reverse('add_programme'))
        else:
            messages.error(request, 'Failed to add programme/service. Please ensure the form is valid.')
    else:
        form = ProgrammeForm()

    template = 'programmes/add_programme.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_programme(request, programme_id):
    """ Edit a programme on the site """
    programme = get_object_or_404(Programme, pk=programme_id)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES, instance=programme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated programme!')
            return redirect(reverse('programme_detail', args=[programme.id]))
        else:
            messages.error(request, 'Failed to update programme. Please ensure the form is valid.')
    else:
        form = ProgrammeForm(instance=programme)
        messages.info(request, f'You are editing {programme.name}')

    template = 'programmes/edit_programme.html'
    context = {
        'form': form,
        'programme': programme,
    }

    return render(request, template, context)
