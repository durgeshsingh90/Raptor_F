from django.db import models

class TextData(models.Model):
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
