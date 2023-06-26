from django.shortcuts import render

from .models import Coffee, Employee

# Create your views here.
def index(request):
    return render(request, "coffees/index.html", {
        "coffees": Coffee.objects.all()
    })

def employees(request):
    return render(request, "coffees/employees.html", {
        "employees": Employee.objects.all()
    })