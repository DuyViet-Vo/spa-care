from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.users.models import User

from .serializers import RegistrationSerializer, UpdateUserSerializer, UserSerializer


class UserRegisterView(CreateAPIView):
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


class ListUserView(ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination


class UpdateUserView(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    lookup_field = "id"
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
