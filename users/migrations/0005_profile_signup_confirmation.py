# Generated by Django 4.1 on 2022-09-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_profile_is_employer"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="signup_confirmation",
            field=models.BooleanField(default=False),
        ),
    ]
