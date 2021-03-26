from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
