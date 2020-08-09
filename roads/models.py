from django.db import models
from django.contrib.auth.models import User


class Road(models.Model):
    class Status(models.TextChoices):
        SUB = '1', "submitted"
        APP = '2', "approved"
        REJ = '3', "rejected"
        WIP = '4', "workinprogress"
        COM = '5', "completed"


    road_name = models.CharField(max_length=100)

    road_condition = models.CharField(max_length=600, blank=True)

    image = models.FileField(blank=False, null=False, upload_to='user')

    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)

    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)

    predictedImage = models.FileField(blank=True, upload_to="model")

    owner = models.ForeignKey(
        User, related_name='roads', on_delete=models.CASCADE, null=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.SUB)

    isRealTime = models.BooleanField(blank=True, default=False)

    PCI = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)



    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.road_name
