from django.db import models
from django.utils import timezone
# Create your models here.
class ProjectsDetails(models.Model):
    project_title = models.CharField(max_length=150)
    project_description = models.TextField()
    project_date = models.CharField(max_length=25)
    project_image = models.ImageField(upload_to="static/ProjectHeroImages")
    author_name = models.CharField(max_length=150, default="Ayush")
    project_url = models.TextField()