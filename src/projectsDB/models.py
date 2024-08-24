from django.db import models
from django.utils import timezone
# Create your models here.
class ProjectsDetails(models.Model):
    project_title = models.CharField(max_length=150)
    project_description = models.TextField()
    project_date = models.TextField(default=timezone.now)
    project_image = models.ImageField(upload_to="ProjectHeroImages")
    project_url = models.TextField()