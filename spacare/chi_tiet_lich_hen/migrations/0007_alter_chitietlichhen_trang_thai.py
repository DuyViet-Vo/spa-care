# Generated by Django 4.2.6 on 2024-01-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chi_tiet_lich_hen", "0006_alter_chitietlichhen_ghi_chu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chitietlichhen",
            name="trang_thai",
            field=models.CharField(
                choices=[
                    ("Chưa Thực Hiện", "chua_thuc_hien"),
                    ("Đang Thực Hiện", "dang_thuc_hien"),
                    ("Đã hoàn thành", "da_hoan_thanh"),
                ],
                default="Chưa Thực Hiện",
                max_length=255,
            ),
        ),
    ]