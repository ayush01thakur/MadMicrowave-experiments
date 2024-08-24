from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# from visits.models import translatorVisits

# from . import utils


def home(request):

    return render(request, 'home.html')


def projects(request):

    return render(request, 'projects.html')
    