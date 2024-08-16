from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home(request):
    queryset = PageVisit.objects.all()
    PageVisit.objects.create()
    context = {
               "pageVisitCount": queryset.count(),

               }
    
    return render(request, 'home.html', context)