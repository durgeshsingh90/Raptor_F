# bitmap_config/models.py

from django.db import models

class Bitmap60Config(models.Model):
    subfield = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    format = models.CharField(max_length=10)
    length_type = models.CharField(max_length=10, blank=True, null=True)
    length = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.subfield
