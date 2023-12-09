from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.dich_vu.models import DichVu
from spacare.dich_vu.serializers import DichVuSerializer, ReadDichVuSerializer


class ListCreateDichVuView(ListCreateAPIView):
    model = DichVu
    serializer_class = DichVuSerializer
    queryset = DichVu.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadDichVuSerializer
        return DichVuSerializer


class UpdateDeleteDichVuView(RetrieveUpdateDestroyAPIView):
    serializer_class = DichVuSerializer
    lookup_field = "id"
    queryset = DichVu.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadDichVuSerializer
        return DichVuSerializer
