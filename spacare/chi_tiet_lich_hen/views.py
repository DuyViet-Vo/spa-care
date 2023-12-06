from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen
from spacare.chi_tiet_lich_hen.serializers import ChiTietLichHenSerializer
from spacare.core.pagination import Pagination


class ListCreateChiTietLichHenView(ListCreateAPIView):
    model = ChiTietLichHen
    serializer_class = ChiTietLichHenSerializer
    queryset = ChiTietLichHen.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination


class UpdateDeleteChiTietLichHenView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChiTietLichHenSerializer
    lookup_field = "id"
    queryset = ChiTietLichHen.objects.all()
    permission_classes = [IsAuthenticated]
