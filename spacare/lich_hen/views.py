from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from spacare.core.pagination import Pagination
from spacare.lich_hen.models import LichHen
from spacare.lich_hen.serializers import LichHenSerializer, ReadLichHenSerializer
from spacare.lich_hen.services import online_payment
from spacare.users.models import User


class ListCreateLichHenView(ListCreateAPIView):
    model = LichHen
    serializer_class = LichHenSerializer
    queryset = LichHen.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["khach_hanh", "trang_thai"]
    search_fields = ["khach_hanh__ho_ten", "khach_hanh__sdt"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadLichHenSerializer
        return LichHenSerializer

    def post(self, request, *args, **kwargs):
        serializer = LichHenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            tien_coc = serializer.data["tien_coc"]

            data_khach_hang = User.objects.filter(
                id=serializer.data["khach_hanh"]
            ).first()
            print("++", data_khach_hang.ho_ten)
            khach_hang = data_khach_hang.ho_ten
            response = online_payment(tien_coc, khach_hang)
            if response.status_code == 201:
                approval_url = response.json()["links"][1]["href"]
                data_response = {"url": approval_url, "id": serializer.data["id"]}
                return Response(data_response)
            else:
                return Response(response.status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteLichHenView(RetrieveUpdateDestroyAPIView):
    serializer_class = LichHenSerializer
    lookup_field = "id"
    queryset = LichHen.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadLichHenSerializer
        return LichHenSerializer
