# Generated by Django 5.2 on 2025-06-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0012_rename_intrests_interests_experience_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
