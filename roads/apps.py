from django.apps import AppConfig
from _io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class RoadsConfig(AppConfig):
    name = 'roads'

    @staticmethod
    def predict(image):
        # ML Model
        file = ContentFile(image.read())
        path = default_storage.save(
            'model/' + str(image), ContentFile('media/user/Screenshot_from_2020-06-06_23-45-11.png'))
        print(path)
        return path
