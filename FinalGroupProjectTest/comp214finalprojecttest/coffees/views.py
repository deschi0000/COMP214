from django.shortcuts import render

from .models import Coffee

# Create your views here.
def index(request):
    return render(request, "coffees/index.html", {
        "coffees": Coffee.objects.all()
    })