from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home(request):
    return HttpResponse("Welcome Home!")
