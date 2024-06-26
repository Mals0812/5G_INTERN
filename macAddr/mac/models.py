
# Create your models here.
from django.db import models


class hub_status(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mac_address