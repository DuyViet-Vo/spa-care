# Generated by Django 4.2.6 on 2023-12-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dich_vu", "0002_dichvu_selected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dichvu",
            name="hinh_anh",
            field=models.TextField(max_length=255, null=True),
        ),
    ]
