from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db.models import Count
from datetime import datetime
from dateutil.parser import *
from django.db import connection
# print connection.queries
import re
import bcrypt
import logging
logger = logging.getLogger(__name__)

from .models import User, Poke
# from .models import User

def index(request):
    return render(request, "beltExam2/index.html")


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
        return redirect("/project2/poke")


    return redirect("/project2")



def login(request):
    postData = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }

    results = User.objects.lValidate(postData)


    if results[0]:
        request.session['logged_in_user'] = results[1].id

        return redirect("/project2/poke")

    else:
        messages.error(request, results[1])
        return redirect("/project2")


def poke(request):
    user_id = request.session['logged_in_user']
    user = User.objects.get(id = request.session['logged_in_user'])


    everything = Poke.objects.all()

    poker_history = User.objects.filter(poker_key__poked=user).annotate(counting=Count("poker_key__poked"))

    test = Poke.objects.filter(poked=user).values('poker__name').distinct().count()
    poked_history = User.objects.filter(poked_key__poker=user).annotate(counting=Count("poked_key__poker"))

    others = User.objects.annotate(poked_history=Count('poked_key')).all().exclude(id=request.session['logged_in_user'])



    context={
        'user': user,
        'test': test,
        'poker_history': poker_history,
        'poked_history': poked_history,
        'others': others,
        'everything': everything,
        # 'manytomany': manytomany,
        # 'user_poked': user_poked,
    }

    return render(request, "beltExam2/poke.html", context)

def logout(request):
    auth.logout(request)
    return redirect("/project2")


def poking(request, id):
    user = User.objects.get(id = request.session['logged_in_user'])
    user_being_poked = User.objects.get(id=id)
    Poke.objects.create(poker=user, poked=user_being_poked)


    user.poked.add(user_being_poked)
    user.save()

    return redirect('/project2/pokes')
