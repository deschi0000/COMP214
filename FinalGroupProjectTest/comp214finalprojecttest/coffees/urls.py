from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employees", views.employees, name="employees"),
    path("add", views.add_coffee, name="add-coffee"),
    path("edit/<str:coffee_id>", views.edit_coffee, name="edit-coffee"),
]