# Generated by Django 4.2.6 on 2023-12-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dich_vu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dichvu",
            name="selected",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
