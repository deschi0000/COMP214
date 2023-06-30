from django import forms
from django.forms import ModelForm

from .models import Coffee

class NewCoffeeForm(ModelForm):
    class Meta:
        model = Coffee

        fields = {"name", "origin", "price"}

        labels = {
            "name": "",
            "origin": "",
            "price": ""
        }

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Coffee Name"}),
            "origin": forms.TextInput(attrs={"class":"form-control", "placeholder":"Origin"}),
            "price": forms.TextInput(attrs={"class":"form-control", "placeholder":"Price"})
        }