from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.dich_vu.models import DichVu
from spacare.dich_vu.serializers import DichVuSerializer


class ListCreateDichVuView(ListCreateAPIView):
    model = DichVu
    serializer_class = DichVuSerializer
    queryset = DichVu.objects.all()
    pagination_class = Pagination


class UpdateDeleteDichVuView(RetrieveUpdateDestroyAPIView):
    serializer_class = DichVuSerializer
    lookup_field = "id"
    queryset = DichVu.objects.all()
    permission_classes = [IsAuthenticated]
