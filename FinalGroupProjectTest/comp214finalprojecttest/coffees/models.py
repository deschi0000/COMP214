from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=64)
    origin = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"Name: {self.name}\nOrigin: {self.origin}\nPrice: {self.price}"

class Location(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    coffees = models.ManyToManyField(Coffee, blank=True, related_name="coffees")
    
    def __str__(self):
        return f"Name: {self.name}\nCity: {self.city}\nCountry: {self.country}"

class Employee(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    workplace = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="workplace")

    def __str__(self):
        return f"First Name: {self.fname}\nLast Name: {self.lname}\nEmail: {self.email}"