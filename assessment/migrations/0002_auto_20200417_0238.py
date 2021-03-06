# Generated by Django 3.0.2 on 2020-04-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='description',
            field=models.TextField(blank=True, max_length=512, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='assessment name'),
        ),
    ]
