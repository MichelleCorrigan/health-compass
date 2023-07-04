from django.shortcuts import render, get_object_or_404
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
    form = ProgrammeForm()
    template = 'programmes/add_programme.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
