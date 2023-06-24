from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=64)
    origin = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"Name: {self.name}\nOrigin: {self.origin}\nPrice: {self.price}"
