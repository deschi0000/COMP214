from django import forms
from django.forms import ModelForm

from .models import Coffee, Employee, Location

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




class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = {"fname", "lname", "email", "workplace"}

        labels = {
            "fname": "",
            "lname": "",
            "email": "",
            "workplace": ""
        }

        widgets = {
            "fname": forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            "lname": forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            "email": forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}),
            "workplace": forms.Select(attrs={"class":"form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Retrieve objects from the database
        workplaces = Location.objects.all()

        # Generate choices based on the retrieved objects
        choices = [(workplace.id, workplace.name) for workplace in workplaces]

        # Set the choices for the field
        self.fields['workplace'].choices = choices