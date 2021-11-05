# Generated by Django 3.0 on 2020-03-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, help_text='Shows whether this user is a student. ', verbose_name='student status'),
        ),
    ]
