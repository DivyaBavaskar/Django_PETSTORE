# Generated by Django 4.2.7 on 2024-02-01 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("petsapp", "0003_cartitem_remove_order_customer_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cartitem",
            options={},
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="pet",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="petsapp.pet"
            ),
        ),
        migrations.CreateModel(
            name="Customer1",
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
                ("phone", models.CharField(default="NA", max_length=10)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cartitem",
            name="customer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="petsapp.customer1",
            ),
            preserve_default=False,
        ),
    ]
