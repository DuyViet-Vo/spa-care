# Generated by Django 4.2.6 on 2024-01-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("combo", "0002_combo_hinh_anh"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="selected",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]