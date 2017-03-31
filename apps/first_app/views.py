from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def test(request):
    response = "Hello I am your first request!"
    return HttpResponse(response)
