from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import generics, status

from .serializers import RegistrationSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )
            serializer.save()

            return JsonResponse(
                {"message": "Register successful!"}, status=status.HTTP_201_CREATED
            )

        else:
            return JsonResponse(
                {
                    "error_message": "This email has already exist!",
                    "errors_code": 400,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
