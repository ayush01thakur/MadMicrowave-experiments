from django.db import models
from django.utils import timezone


# Create your models here.
class ProjectsDetails(models.Model):
    project_title = models.CharField(max_length=150)
    project_description = models.TextField()
    project_date = models.CharField(max_length=25)
    project_image = models.ImageField(upload_to="staticfiles/ProjectHeroImages")
    author_name = models.CharField(max_length=150, default="Ayush")
    project_url = models.TextField()



# project visits tables:

# this one is old method
# class translatorVisits(models.Model):
#     # id -> hidden primary key ->autofiled -> 1,2,3,...
#     path = models.TextField(null=True, blank=True)
#     timestamp =  models.DateTimeField(auto_now_add=True)

class translatorVisits(models.Model):
    path = models.TextField(null=True, blank=True)
    visits = models.IntegerField()