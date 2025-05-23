# Generated by Django 3.2.25 on 2025-04-10 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HR",
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
                ("company_name", models.CharField(max_length=100)),
                ("company_nip", models.CharField(max_length=20)),
                ("telephone", models.CharField(max_length=9)),
                ("city", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("number_street", models.CharField(max_length=5)),
                ("postcode", models.CharField(max_length=10)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
