from django.db import models

# Create your models here.
# class translatorVisits(models.Model):
#     # id -> hidden primary key ->autofiled -> 1,2,3,...
#     path = models.TextField(null=True, blank=True)
#     timestamp =  models.DateTimeField(auto_now_add=True)

class translatorVisitsNew(models.Model):
    path = models.TextField(null=True, blank=True)
    visits = models.IntegerField()