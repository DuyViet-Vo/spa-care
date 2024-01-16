from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spacare.combo.models import Combo
from spacare.combo.serializers import ComboSerializer, ReadComboSerializer
from spacare.core.pagination import Pagination


class ListCreateComboView(ListCreateAPIView):
    model = Combo
    serializer_class = ComboSerializer
    queryset = Combo.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadComboSerializer
        return ComboSerializer


class UpdateDeleteComboView(RetrieveUpdateDestroyAPIView):
    serializer_class = ComboSerializer
    lookup_field = "id"
    queryset = Combo.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadComboSerializer
        return ComboSerializer
