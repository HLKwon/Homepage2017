from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# from collection.forms import ContactForm
import re

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def about(request):
    return render(request, "first_app/about.html")

def projects(request):
    return render(request, "first_app/projects.html")

def contact(request):
    # form_class = ContactForm

    return render(request, 'first_app/contact.html', {
        # 'form': form_class,
    })



def test(request):
    response = "Hello I am your first request!"
    return HttpResponse(response)
