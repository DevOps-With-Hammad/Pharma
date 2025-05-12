from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('The main Index for <h1> Accounts </h1> \n Powered By ,<h4> Django Hammad </h4> ')