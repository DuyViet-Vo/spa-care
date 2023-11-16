from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.quyen.models import Quyen
from spacare.quyen.serializers import QuyenSerializer


class ListCreateQuyenView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    model = Quyen
    serializer_class = QuyenSerializer
    queryset = Quyen.objects.all()


class UpdateDeleteQuyenView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuyenSerializer
    lookup_field = "id"
    queryset = Quyen.objects.all()
    permission_classes = [IsAuthenticated]
