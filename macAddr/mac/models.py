# """model of the database"""
# from django.db import models
# #Create your models here
# class hub_status(models.Model):
#     """Model to represent the status of a hub."""
#     mac_address = models.CharField(max_length=17, unique=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         """Return the MAC address as the string representation of the model."""
#         return self.mac_address
"""Model of the database."""
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here
# pylint: disable=too-few-public-methods
class HubStatus(models.Model):
    """Model to represent the status of a hub."""
    mac_address = models.CharField(max_length=17, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.mac_address)
    def save(self, *args, **kwargs):
        if not self.mac_address:
            raise ValidationError("MAC address is required")
        super().save(*args, **kwargs)
    def formatted_timestamp(self):
        """Return the timestamp formatted as a string."""
        return timezone.localtime(self.timestamp).strftime("%Y-%m-%d %H:%M:%S")
    def is_recent(self):
        """Check if the status timestamp is recent."""
        now = timezone.now()
        return now - self.timestamp < timezone.timedelta(days=1)
    class Meta:
        """Meta options for the HubStatus model."""
        verbose_name = "Hub Status"
        verbose_name_plural = "Hub Statuses"
