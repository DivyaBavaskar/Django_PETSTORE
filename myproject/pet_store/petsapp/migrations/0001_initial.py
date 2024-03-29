# Generated by Django 4.2.7 on 2023-11-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="media")),
                ("name", models.CharField(max_length=150)),
                ("breed", models.CharField(max_length=150)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")], max_length=30
                    ),
                ),
                ("description", models.CharField(max_length=500)),
                ("price", models.IntegerField()),
            ],
        ),
    ]
