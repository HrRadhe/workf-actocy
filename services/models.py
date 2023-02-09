from django.db import models
from serviceman.models import Serviceman

class MainService(models.Model):
    serviceman = models.OneToOneField(Serviceman, on_delete=models.CASCADE)
    user = models.CharField(default=serviceman, max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.serviceman.user.phone_number

class SubService(models.Model):
    user = models.OneToOneField(MainService, on_delete=models.CASCADE)
    serviceman = models.OneToOneField(Serviceman, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.serviceman.user.phone_number
