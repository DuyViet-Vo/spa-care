from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen
from spacare.chi_tiet_lich_hen.serializers import (
    BulkChiTietLichHenSerializer,
    ChiTietLichHenSerializer,
    ReadChiTietLichHenSerializer,
)
from spacare.core.pagination import Pagination


class BulkCreateChiTietLichHenView(CreateAPIView):
    serializer_class = BulkChiTietLichHenSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        if len(data) == 0:
            raise ParseError("nhap data!")
        serializer = BulkChiTietLichHenSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class ListCreateChiTietLichHenView(ListCreateAPIView):
    model = ChiTietLichHen
    serializer_class = ChiTietLichHenSerializer
    queryset = ChiTietLichHen.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["lich_hen__khach_hanh__id", "trang_thai", "nhan_vien"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadChiTietLichHenSerializer
        return ChiTietLichHenSerializer


class UpdateDeleteChiTietLichHenView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChiTietLichHenSerializer
    lookup_field = "id"
    queryset = ChiTietLichHen.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadChiTietLichHenSerializer
        return ChiTietLichHenSerializer
