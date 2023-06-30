from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Coffee, Employee
from .forms import NewCoffeeForm

# Create your views here.
def index(request):
    return render(request, "coffees/index.html", {
        "coffees": Coffee.objects.all()
    })

def employees(request):
    return render(request, "coffees/employees.html", {
        "employees": Employee.objects.all()
    })

# ADD
def add_coffee(request):
    if request.method == "POST":
        newcoffee = NewCoffeeForm(request.POST)

        if newcoffee.is_valid():
            obj = newcoffee
            obj.save()

        return HttpResponseRedirect(reverse("index"))
    
    # New coffee Form
    form = NewCoffeeForm

    return render(request, "coffees/addcoffee.html", {
        "form": form
    })

# UPDATE
def edit_coffee(request, coffee_id):
    coffee_to_edit = Coffee.objects.get(id=coffee_id)

    
    if request.method == "POST":
        newcoffee = NewCoffeeForm(request.POST, instance=coffee_to_edit)

        if "delete" in request.POST:
            print("trying to delete: " + coffee_id)
            coffee_to_edit.delete()
            return redirect("index")
        else:

            if newcoffee.is_valid():
                newcoffee.save()
                return HttpResponseRedirect(reverse("index"))
            else:
                newcoffee = NewCoffeeForm(instance=coffee_to_edit)
        
    form = NewCoffeeForm(instance=coffee_to_edit)
    return render(request, "coffees/editcoffee.html", {
        "coffee": coffee_to_edit,
        "form": form
    })
