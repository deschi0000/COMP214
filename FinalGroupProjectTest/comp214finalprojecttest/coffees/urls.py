from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addcoffee", views.add_coffee, name="add-coffee"),
    path("employees", views.employees, name="employees"),
    path("addemployee", views.add_employee, name="add-employee"),
    path("locations", views.location_list, name="locations"),
    path("edit/<str:coffee_id>", views.edit_coffee, name="edit-coffee"),
    path("location/<str:location_id>", views.location, name="location"),

]