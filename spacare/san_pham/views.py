from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.san_pham.models import SanPham
from spacare.san_pham.serializers import ReadSanPhamSerializer, SanPhamSerializer


class ListCreateSanPhamView(ListCreateAPIView):
    model = SanPham
    serializer_class = SanPhamSerializer
    queryset = SanPham.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadSanPhamSerializer
        return SanPhamSerializer


class UpdateDeleteSanPhamView(RetrieveUpdateDestroyAPIView):
    serializer_class = SanPhamSerializer
    lookup_field = "id"
    queryset = SanPham.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadSanPhamSerializer
        return SanPhamSerializer
