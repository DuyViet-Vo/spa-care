from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.chi_tiet_combo.models import ChiTietCombo
from spacare.chi_tiet_combo.serializers import ChiTietComboSerializer
from spacare.core.pagination import Pagination


class ListCreateChiTietComboView(ListCreateAPIView):
    model = ChiTietCombo
    serializer_class = ChiTietComboSerializer
    queryset = ChiTietCombo.objects.all()
    pagination_class = Pagination


class UpdateDeleteChiTietComboView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChiTietComboSerializer
    lookup_field = "id"
    queryset = ChiTietCombo.objects.all()
    permission_classes = [IsAuthenticated]
