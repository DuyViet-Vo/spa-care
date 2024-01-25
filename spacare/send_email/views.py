import os

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen
from spacare.chi_tiet_lich_hen.serializers import ReadChiTietLichHenSerializer
from spacare.lich_hen.models import LichHen
from spacare.lich_hen.serializers import ReadLichHenSerializer
from spacare.send_email.serializers import SendEmailLichHen, SendEmialChiTiet
from spacare.send_email.services import convert_datetime, create_pdf, format_number
from spacare.users.models import User


class SendEmailView(CreateAPIView):
    serializer_class = SendEmailLichHen
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendEmailLichHen(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_lich_hen = serializer.validated_data.get("id_lich_hen")
        lich_hen = LichHen.objects.filter(id=id_lich_hen).first()

        if not lich_hen:
            return Response({"message": "LichHen not found"}, status=404)

        data_lich_hen = ReadLichHenSerializer(instance=lich_hen).data

        ten = data_lich_hen["khach_hanh"]["ho_ten"]
        mail_to = data_lich_hen["khach_hanh"]["email"]
        sdt = data_lich_hen["khach_hanh"]["sdt"]
        thoi_gian_hen = convert_datetime(data_lich_hen["thoi_gian_hen"])
        chi_tiet_lich_hen = data_lich_hen["chi_tiet_lich_hen"]
        tong_tien = format_number(data_lich_hen["tong_tien"])
        products = []
        stt = 0
        dich_vu_mail = ""
        for chi_tiet in chi_tiet_lich_hen:
            stt = stt + 1
            product = {
                "stt": stt,
                "dich_vu": chi_tiet["dich_vu"]["ten_dich_vu"],
                "trang_thai": chi_tiet["trang_thai"],
                "ghi_chu": chi_tiet["ghi_chu"],
            }
            dich_vu_mail += chi_tiet["dich_vu"]["ten_dich_vu"] + "; "
            products.append(product)
        # Create PDF file
        pdf_filename = create_pdf(ten, sdt, thoi_gian_hen, products, tong_tien)

        mail_from = settings.EMAIL_HOST_USER

        subject = "THÔNG BÁO LICH HEN"
        text_content = "This is an important message."
        content = {
            "ho_ten": ten,
            "thoi_gian_hen": thoi_gian_hen,
            "dich_vu": dich_vu_mail,
        }

        # Render HTML content
        html_content = render_to_string("lich_hen_da_duyet.html", context=content)

        # Create EmailMultiAlternatives instance
        msg = EmailMultiAlternatives(subject, text_content, mail_from, [mail_to])

        # Attach HTML content
        msg.attach_alternative(html_content, "text/html")
        # Attach PDF file
        with open(pdf_filename, "rb") as pdf_file:
            msg.attach_file(pdf_file.name)

        # Send the email
        msg.send()

        # Delete the PDF file after sending the email
        os.remove(pdf_filename)

        return Response(
            {"message": "Email sent successfully"}, status=status.HTTP_200_OK
        )


class SendEmailChuaDuyet(CreateAPIView):
    serializer_class = SendEmailLichHen
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendEmailLichHen(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_lich_hen = serializer.validated_data.get("id_lich_hen")
        lich_hen = LichHen.objects.filter(id=id_lich_hen).first()

        if not lich_hen:
            return Response({"message": "LichHen not found"}, status=404)

        data_lich_hen = ReadLichHenSerializer(instance=lich_hen).data
        ten = data_lich_hen["khach_hanh"]["ho_ten"]
        mail_to = data_lich_hen["khach_hanh"]["email"]
        thoi_gian_hen = convert_datetime(data_lich_hen["thoi_gian_hen"])
        tong_tien = format_number(data_lich_hen["tong_tien"])
        chi_tiet_lich_hen = data_lich_hen["chi_tiet_lich_hen"]

        dich_vu_mail = ""
        for chi_tiet in chi_tiet_lich_hen:
            dich_vu_mail += chi_tiet["dich_vu"]["ten_dich_vu"] + "; "

        mail_from = settings.EMAIL_HOST_USER
        subject = "THÔNG BÁO LICH HEN"
        content = {
            "ho_ten": ten,
            "thoi_gian_hen": thoi_gian_hen,
            "dich_vu": dich_vu_mail,
            "tong_tien": tong_tien,
        }
        # Render HTML content
        html_content = render_to_string("lich_hen_chua_duyet.html", context=content)
        msg = EmailMultiAlternatives(subject, None, mail_from, [mail_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response(
            {"message": "Email sent successfully"}, status=status.HTTP_200_OK
        )


class SendEmailThucHien(CreateAPIView):
    serializer_class = SendEmialChiTiet
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendEmialChiTiet(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_chi_tiet = serializer.validated_data.get("id_chi_tiet")
        chi_tiet_lich_hen = ChiTietLichHen.objects.filter(id=id_chi_tiet).first()

        if not chi_tiet_lich_hen:
            return Response({"message": "LichHen not found"}, status=404)

        data_chi_tiet = ReadChiTietLichHenSerializer(instance=chi_tiet_lich_hen).data
        id_khach_hang = data_chi_tiet["lich_hen"]["khach_hanh"]
        nhan_vien = data_chi_tiet["nhan_vien"]["ho_ten"]
        dich_vu = data_chi_tiet["dich_vu"]["ten_dich_vu"]
        khachang = User.objects.filter(id=id_khach_hang).first()

        mail_from = settings.EMAIL_HOST_USER
        subject = "THÔNG BÁO LICH HEN"
        content = {
            "nhan_vien": nhan_vien,
            "dich_vu": dich_vu,
        }
        # Render HTML content
        html_content = render_to_string("thuc_hien.html", context=content)
        msg = EmailMultiAlternatives(subject, None, mail_from, [khachang])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response(
            {"message": "Email sent successfully"}, status=status.HTTP_200_OK
        )


class SendEmailDaThucHien(CreateAPIView):
    serializer_class = SendEmialChiTiet
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendEmialChiTiet(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_chi_tiet = serializer.validated_data.get("id_chi_tiet")
        chi_tiet_lich_hen = ChiTietLichHen.objects.filter(id=id_chi_tiet).first()

        if not chi_tiet_lich_hen:
            return Response({"message": "LichHen not found"}, status=404)

        data_chi_tiet = ReadChiTietLichHenSerializer(instance=chi_tiet_lich_hen).data
        id_khach_hang = data_chi_tiet["lich_hen"]["khach_hanh"]
        nhan_vien = data_chi_tiet["nhan_vien"]["ho_ten"]
        dich_vu = data_chi_tiet["dich_vu"]["ten_dich_vu"]
        khachang = User.objects.filter(id=id_khach_hang).first()

        mail_from = settings.EMAIL_HOST_USER
        subject = "THÔNG BÁO LICH HEN"
        content = {
            "nhan_vien": nhan_vien,
            "dich_vu": dich_vu,
        }
        # Render HTML content
        html_content = render_to_string("da_thuc_hien.html", context=content)
        msg = EmailMultiAlternatives(subject, None, mail_from, [khachang])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response(
            {"message": "Email sent successfully"}, status=status.HTTP_200_OK
        )
