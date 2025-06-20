# Generated by Django 5.2 on 2025-06-05 21:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0003_alter_cvinfo_avatar_contact_contactlinks_experience_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactlinks",
            name="link",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="contactlinks",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="cvinfo",
            name="avatar",
            field=models.ImageField(
                null=True,
                upload_to="<function CustomUser.get_id at 0x00000151C08349A0>/",
            ),
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("institution", models.CharField(max_length=255)),
                ("degree", models.CharField(max_length=255)),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "cv_info_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cv.cvinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HardSkills",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("skill", models.CharField(max_length=255)),
                (
                    "cv_info_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cv.cvinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Intrests",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("interest", models.CharField(max_length=255)),
                (
                    "cv_info_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cv.cvinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("language", models.CharField(max_length=100)),
                ("language_lever", models.CharField(max_length=50)),
                (
                    "cv_info_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cv.cvinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SoftSkills",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("skill", models.CharField(max_length=255)),
                (
                    "cv_info_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cv.cvinfo"
                    ),
                ),
            ],
        ),
    ]
