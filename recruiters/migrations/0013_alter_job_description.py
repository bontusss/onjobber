# Generated by Django 4.1 on 2022-08-25 13:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0012_job_recruiter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
