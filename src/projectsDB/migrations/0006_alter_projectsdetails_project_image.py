# Generated by Django 5.0.8 on 2024-08-25 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectsDB", "0005_translatorvisits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectsdetails",
            name="project_image",
            field=models.ImageField(upload_to="staticfiles/ProjectHeroImages"),
        ),
    ]
