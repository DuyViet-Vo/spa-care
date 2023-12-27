from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from spacare.send_email.serializers import EmailSend


class SendEmailView(CreateAPIView):
    serializer_class = EmailSend

    def post(self, request, *args, **kwargs):
        serializer = EmailSend(data=request.data)
        if serializer.is_valid():
            mail_from = settings.EMAIL_HOST_USER
            mail_to = serializer.validated_data.get("to_email")
            subject = "THÔNG BÁO LICH HEN"
            text_content = "This is an important message."
            # Provide the correct template name in the render_to_string function
            html_content = "<h2>Thông báo lịch hẹn</h2>"

            msg = EmailMultiAlternatives(subject, text_content, mail_from, [mail_to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return Response({"message": "Email sent successfully"})
        return Response(serializer.errors, status=400)
