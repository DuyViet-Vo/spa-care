from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.lich_hen.models import LichHen
from spacare.lich_hen.serializers import LichHenSerializer, ReadLichHenSerializer


class ListCreateLichHenView(ListCreateAPIView):
    model = LichHen
    serializer_class = LichHenSerializer
    queryset = LichHen.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["khach_hanh", "trang_thai"]
    search_fields = ["khach_hanh__ho_ten", "khach_hanh__sdt"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadLichHenSerializer
        return LichHenSerializer


class UpdateDeleteLichHenView(RetrieveUpdateDestroyAPIView):
    serializer_class = LichHenSerializer
    lookup_field = "id"
    queryset = LichHen.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadLichHenSerializer
        return LichHenSerializer
