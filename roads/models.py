from django.db import models
from django.contrib.auth.models import User


class Road(models.Model):
    road_name = models.CharField(max_length=100)
    road_condition = models.CharField(max_length=600, blank=True)
    image = models.FileField(blank=False, null=False)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    owner = models.ForeignKey(
        User, related_name='roads', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.road_name
