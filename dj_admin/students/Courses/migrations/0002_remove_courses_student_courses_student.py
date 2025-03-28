# Generated by Django 5.1.3 on 2024-11-16 05:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='student',
        ),
        migrations.AddField(
            model_name='courses',
            name='student',
            field=models.ManyToManyField(related_name='enrolled_courses', to=settings.AUTH_USER_MODEL, verbose_name='Student Name'),
        ),
    ]
