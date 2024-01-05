import os

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from spacare.lich_hen.models import LichHen
from spacare.lich_hen.serializers import ReadLichHenSerializer
from spacare.send_email.serializers import SendEmailLichHen
from spacare.send_email.services import convert_datetime, create_pdf


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
        sdt = data_lich_hen["khach_hanh"]["sdt"]
        thoi_gian_hen = convert_datetime(data_lich_hen["thoi_gian_hen"])
        chi_tiet_lich_hen = data_lich_hen["chi_tiet_lich_hen"]

        products = []
        stt = 0
        for chi_tiet in chi_tiet_lich_hen:
            stt = stt + 1
            product = {
                "stt": stt,
                "dich_vu": chi_tiet["dich_vu"]["ten_dich_vu"],
                "trang_thai": chi_tiet["trang_thai"],
                "ghi_chu": chi_tiet["ghi_chu"],
            }
            products.append(product)

        # Create PDF file
        pdf_filename = create_pdf(ten, sdt, thoi_gian_hen, products)

        mail_from = settings.EMAIL_HOST_USER
        mail_to = self.request.user.email
        name = self.request.user.ho_ten
        subject = "THÔNG BÁO LICH HEN"
        text_content = "This is an important message."
        content = {
            "code": "123123",
            "time": "11h11 20/10/2023",
            "email": name,
        }

        # Render HTML content
        html_content = render_to_string("lich_hen.html", context=content)

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
