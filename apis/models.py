from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.TextField()