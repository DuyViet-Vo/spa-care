# Generated by Django 4.2.6 on 2024-01-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("combo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="hinh_anh",
            field=models.TextField(null=True),
        ),
    ]