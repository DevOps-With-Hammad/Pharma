from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (request):
    return  HttpResponse("<h1> اهلا ومرحبا معاكم البنجز وانجز </h1>")

def about (request):
    return HttpResponse("<h1> About Page  </h1>")