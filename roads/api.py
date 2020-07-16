from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser
from .models import Road
from .serializers import RoadSerializer


# Road Serializers
class RoadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    parser_class = (FileUploadParser,)

    serializer_class = RoadSerializer

    def get_queryset(self):
        return self.request.user.roads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
