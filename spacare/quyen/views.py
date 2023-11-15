from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.quyen.models import Quyen
from spacare.quyen.serializers import QuyenSerializer


class LisCreateQuyenView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    model = Quyen
    serializer_class = QuyenSerializer
    queryset = Quyen.objects.all()
