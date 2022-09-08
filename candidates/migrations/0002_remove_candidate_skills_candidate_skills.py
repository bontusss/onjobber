# Generated by Django 4.1 on 2022-08-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0002_category_job_category"),
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="skills",
        ),
        migrations.AddField(
            model_name="candidate",
            name="skills",
            field=models.ManyToManyField(to="recruiters.skill"),
        ),
    ]
