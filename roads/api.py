from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser
from .models import Road
from .serializers import RoadSerializer
from .apps import RoadsConfig

from .model.load_model import Model

m = Model()
m.load()

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

        # newImage = RoadsConfig.predict(self.request.data['image'])

        result_path , scores, pci = m.predict(self.request.data['image'])
        print(result_path)
        print(scores)

        if len(scores) == 0:
            status = "3"
        else:
            status = "1"

        serializer.save(owner=self.request.user, predictedImage=result_path[6:]+'.png', status=status, PCI=pci)
