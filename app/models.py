from django import shortcuts
from django.db import models

# Create your models here.

class MappingUrl(models.Model):
    created = models.DateTimeField(auto_now=True)
    originUrl = models.URLField(primary_key=True)
    shortenString = models.CharField(max_length=8)