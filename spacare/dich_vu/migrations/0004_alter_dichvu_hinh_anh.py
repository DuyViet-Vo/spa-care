# Generated by Django 4.2.6 on 2023-12-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dich_vu", "0003_alter_dichvu_hinh_anh"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dichvu",
            name="hinh_anh",
            field=models.TextField(null=True),
        ),
    ]
