from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spacare.core.pagination import Pagination
from spacare.uu_dai.models import UuDai
from spacare.uu_dai.serializers import UuDaiSerializer


class ListCreateUuDaiView(ListCreateAPIView):
    model = UuDai
    serializer_class = UuDaiSerializer
    queryset = UuDai.objects.all()
    pagination_class = Pagination


class UpdateDeleteUuDaiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UuDaiSerializer
    lookup_field = "id"
    queryset = UuDai.objects.all()
    permission_classes = [IsAuthenticated]
