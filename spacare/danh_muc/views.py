from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.danh_muc.models import DanhMuc
from spacare.danh_muc.serializers import DanhMucSerializer


class ListCreateDanhMucView(ListCreateAPIView):
    model = DanhMuc
    serializer_class = DanhMucSerializer
    queryset = DanhMuc.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination


class UpdateDeleteDanhMucView(RetrieveUpdateDestroyAPIView):
    serializer_class = DanhMucSerializer
    lookup_field = "id"
    queryset = DanhMuc.objects.all()
    permission_classes = [IsAuthenticated]
