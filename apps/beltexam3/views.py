from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db.models import Count
from datetime import datetime
from dateutil.parser import *
from django.db import connection
import re
import bcrypt

from .models import Quotes, Favorites, User

# Create your views here.

def index(request):

    return render(request, "beltexam3/index.html")


def register(request):


    postData = {
        'name': request.POST['name'],
        'alias': request.POST['alias'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'cPassword': request.POST['cPassword'],
        'birthday': request.POST['birthday'],
    }

    results = User.objects.rValidate(postData)
    #(True, [err err err])
    #(False, user obj)
    if results[0]: #if flag is True i.e. there is an error
        for err in results[1]: #taking string messages in list error from Models.py
                                #and then repackage them into messages list below
            messages.error(request, err) #django framework messages

    else:
        request.session['logged_in_user'] = results[1].id
        return redirect("/project3/quote")


    return redirect("/project3")



def login(request):
    postData = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }

    results = User.objects.lValidate(postData)


    if results[0]:
        request.session['logged_in_user'] = results[1].id

        return redirect("/project3/quote")

    else:
        messages.error(request, results[1])
        return redirect("/project3")


def quote(request):
    user_id = request.session['logged_in_user']
    user = User.objects.get(id = request.session['logged_in_user'])
    y = Favorites.objects.filter(favorited_by=user).values('favorite__id')


    quotes = Quotes.objects.all().exclude(id__in=y)
    favorites = Favorites.objects.filter(favorited_by=user)

    context={
        'user': user,
        'quotes': quotes,
        'favorites': favorites,
    }

    return render(request, "beltexam3/quote.html", context)


def add(request):
    errors=[]
    flag = False
    if not request.POST['author']:
        errors.append("Quoted by is blank.")
        flag = True
    if not request.POST['quote']:
        errors.append("Message is blank.")
        flag = True
    if flag:
        for err in errors:
            messages.error(request, err)
        return redirect("/project3/quote")

    user = User.objects.get(id = request.session['logged_in_user'])
    author = request.POST['author']
    quote = request.POST['quote']
    Quotes.objects.create(quote=quote, author=author, poster=user)
    return redirect('/project3/quote')


def add_to_list(request, id):
    user = User.objects.get(id = request.session['logged_in_user'])
    quote = Quotes.objects.get(id=id)

    Favorites.objects.create(favorite=quote, favorited_by=user)

    return redirect('/project3/quote')


def remove_from_list(request, id):
    user = User.objects.get(id = request.session['logged_in_user'])
    quote = Quotes.objects.get(id=id)

    favorite_to_be_removed = Favorites.objects.filter(favorited_by=user).filter(favorite=quote)
    favorite_to_be_removed.delete()

    return redirect('/project3/quote')


def logout(request):
    auth.logout(request)
    return redirect("/project3")


def users(request, id):
    person = User.objects.get(id=id)
    quotes = Quotes.objects.filter(poster=person)
    counting = Quotes.objects.filter(poster=person).count()

    context={
        'person': person,
        'counting': counting,
        'quotes': quotes,
    }
    return render(request, "beltexam3/quotes.html", context)
