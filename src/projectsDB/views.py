from django.shortcuts import render, redirect
from decouple import config
from .models import *

# Create your views here.
context={"passOrFail":""}

def addProjects(requests):
    

    if (requests.method == 'POST'):
        data = requests.POST
        project_title = data.get("project_title")
        project_date = data.get("project_date")
        project_description = data.get("project_description")
        project_image = requests.FILES.get("project_image")
        author_name = data.get("author_name")
        project_url = data.get("project_url")
        choco_cookie = data.get("choco_cookie")

        if(choco_cookie== config("CHOCO_ADD_PASS")):
            # upload then only.

            ProjectsDetails.objects.create(
                project_title=project_title,
                project_date= project_date,
                project_description= project_description,
                project_image= project_image,
                project_url = project_url,
                author_name= author_name,
            )

            # print(
            #     project_title,
            #     project_date,
            #     project_description,
            #     project_image,
            #     project_url,
            #     author_name
            # )

            context["passOrFail"]="Success"
            return redirect('/addchocolate/')


        else:
            # send an error message that pass is not correct.
            context["passOrFail"]="Failed"
            return redirect('/addchocolate/')

    return render(requests, 'addProjects.html', context)
