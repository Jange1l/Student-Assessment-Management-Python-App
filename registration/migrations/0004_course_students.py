# Generated by Django 3.0.2 on 2020-04-15 19:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0003_remove_course_professor_eagle_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
