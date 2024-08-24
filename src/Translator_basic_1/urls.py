# Translator_basic_1/urls.py
from django.urls import path
from . import views

app_name= "translator"

urlpatterns = [
    path('translator-70b/', views.translate_70b, name='translator-70b'),
]