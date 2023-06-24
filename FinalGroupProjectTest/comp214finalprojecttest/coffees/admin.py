from django.contrib import admin

# Register your models here.
from .models import Coffee, Location, Employee

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Location)
admin.site.register(Employee)
