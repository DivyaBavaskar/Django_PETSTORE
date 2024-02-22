# Generated by Django 4.2.7 on 2024-02-07 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "petsapp",
            "0004_alter_cartitem_options_alter_cartitem_pet_customer1_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingAddress1",
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
                ("building_name", models.CharField(max_length=300)),
                ("street", models.CharField(blank=True, max_length=200)),
                ("landmark", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(max_length=30)),
                ("zipcode", models.CharField(max_length=8)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="petsapp.customer1",
                    ),
                ),
            ],
        ),
    ]
