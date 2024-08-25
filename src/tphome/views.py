from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from projectsDB.models import ProjectsDetails


def home(request):

    return render(request, 'home.html')


def projects(request):
    all_projects = ProjectsDetails.objects.all().order_by('-id')
    paginator = Paginator(all_projects, 9)  # Show 9 articles per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    print(all_projects[0].project_image)

    context = {
        'projects': projects,
    }


    return render(request, 'projects.html', context)
    