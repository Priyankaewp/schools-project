from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Sample View</h1>")

def products(request):
    return HttpResponse("<h1> Products Page</h1")

def services(request):
    return HttpResponse("<h1> Services Available</h1>")