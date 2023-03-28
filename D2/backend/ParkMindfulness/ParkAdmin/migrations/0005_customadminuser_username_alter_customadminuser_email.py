# Generated by Django 4.1.7 on 2023-03-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ParkAdmin", "0004_remove_customadminuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customadminuser",
            name="username",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="customadminuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
