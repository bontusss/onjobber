# Generated by Django 4.1 on 2022-08-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0003_job_popular"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="category",
        ),
        migrations.RemoveField(
            model_name="job",
            name="skills",
        ),
        migrations.AddField(
            model_name="job",
            name="category",
            field=models.ManyToManyField(null=True, to="recruiters.category"),
        ),
        migrations.AddField(
            model_name="job",
            name="skills",
            field=models.ManyToManyField(null=True, to="recruiters.skill"),
        ),
    ]