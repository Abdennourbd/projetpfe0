# Generated by Django 5.2 on 2025-04-06 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_initial'),
        ('programs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='programmodule',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_modules', to='courses.module'),
        ),
        migrations.AddField(
            model_name='programmodule',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_modules', to='programs.program'),
        ),
        migrations.AddField(
            model_name='programprogress',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='programs.program'),
        ),
        migrations.AddField(
            model_name='programprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_progress', to=settings.AUTH_USER_MODEL),
        ),
    ]
