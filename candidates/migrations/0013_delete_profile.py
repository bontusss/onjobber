# Generated by Django 4.1 on 2022-08-31 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0012_profile_facebook_link_profile_github_link_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]