from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse("Zdravo!")
    return render(request, "hello/index.html")

def mitke(request):
    return HttpResponse("Zdravo, Mitke")

def greet(request, name):
#    return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
