from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



def index(request):
    return render(request, "first_app/index.html")

def about(request):
    return render(request, "first_app/about.html")

def projects(request):
    return render(request, "first_app/projects.html")

def contact(request):

    if request.method == 'POST':
        errors=[]
        flag = False

        if not request.POST['email']:
            errors.append("Email is empty")
            flag = True
        if not request.POST['fname']:
            errors.append("First name is empty")
            flag = True
        if not request.POST['lname']:
            errors.append("Last name is empty")
            flag = True
        if flag:
            for err in errors:
                messages.error(request, err)
            return redirect("contact")

        else:
            messages.success(request, "Contact form was submitted!")

            email = request.POST['email']
            fname = request.POST['fname']
            lname = request.POST['lname']
            message = request.POST['message']

            # Email the profile with the
            # contact information
            template = get_template('first_app/second_contact_template.txt')
            context = Context({
                'email': email,
                'fname': fname,
                'lname': lname,
                'form_message': message
            })
            content = template.render(context)

            emailToSend = EmailMessage(
                "New contact form submission",
                content,
                email,
                ['hannuri.kwon@gmail.com'],
                headers = {'Reply-To': email }
            )
            emailToSend.send()
            return redirect('contact')


    return render(request, 'first_app/contact.html')



def test(request):
    response = "Hello I am your first request!"
    return HttpResponse(response)
