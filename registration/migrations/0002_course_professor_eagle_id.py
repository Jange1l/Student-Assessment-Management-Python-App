# Generated by Django 3.0.2 on 2020-04-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor_eagle_id',
            field=models.CharField(max_length=8, null=True, verbose_name='professor eagle id'),
        ),
    ]
