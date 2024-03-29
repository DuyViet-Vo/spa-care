from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from spacare.users.models import User

from .serializers import (
    CreateNhanVien,
    ReadUserSerializer,
    RegistrationSerializer,
    UpdateUserSerializer,
    UserSerializer,
)


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


class UserView(ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class UpdateUserView(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    lookup_field = "id"
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class ListUserView(ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ["quyen", "trang_thai"]
    search_fields = ["ho_ten", "sdt", "trang_thai"]
    filterset_fields = ["quyen"]


class ListNhanVienView(ListAPIView):
    model = User
    serializer_class = ReadUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    ordering_fields = ["quyen", "trang_thai"]
    search_fields = ["ho_ten", "sdt", "trang_thai"]
    filterset_fields = ["quyen"]

    def get_queryset(self):
        quyen_ids = [2, 3, 4]
        return self.queryset.filter(quyen__id__in=quyen_ids)


class CreateNhanVienView(CreateAPIView):
    serializer_class = CreateNhanVien
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateNhanVien(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        quyen = serializer.validated_data.get("quyen")
        luong = serializer.validated_data.get("luong")
        nhan_vien = User.objects.filter(email=email)
        if not nhan_vien.exists():
            return Response(
                {"message": "User not found with the given email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Nếu có người dùng, thực hiện cập nhật và trả về 200 OK
        nhan_vien.update(quyen_id=quyen, luong=luong)
        return Response(
            {"message": "Create nhan vien successfully"}, status=status.HTTP_200_OK
        )
