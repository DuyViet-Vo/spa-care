# Generated by Django 4.2.6 on 2024-01-05 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("danh_muc", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Combo",
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
                ("ten_combo", models.CharField(max_length=255)),
                ("mo_ta", models.CharField(max_length=255)),
                ("gia", models.BigIntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "danh_muc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="danh_muc_combo",
                        to="danh_muc.danhmuc",
                    ),
                ),
            ],
        ),
    ]
