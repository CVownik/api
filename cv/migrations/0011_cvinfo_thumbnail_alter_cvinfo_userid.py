# Generated by Django 5.2 on 2025-06-07 22:36

import cv.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0010_alter_experience_end_date"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="cvinfo",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to=cv.models.user_avatar_upload_path
            ),
        ),
        migrations.AlterField(
            model_name="cvinfo",
            name="userId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
