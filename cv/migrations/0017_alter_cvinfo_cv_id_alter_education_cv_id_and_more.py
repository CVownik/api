# Generated by Django 5.2 on 2025-06-10 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0016_alter_cvinfo_cv_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cvinfo",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="hardskills",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="interests",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="languages",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
        migrations.AlterField(
            model_name="softskills",
            name="cv_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cv.cv"
            ),
        ),
    ]
