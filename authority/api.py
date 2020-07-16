from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser
from roads.models import Road
from roads.serializers import RoadSerializer


# Road Serializers
class AdminRoadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    parser_class = (FileUploadParser,)

    serializer_class = RoadSerializer

    def get_queryset(self):
        return Road.objects.all()

