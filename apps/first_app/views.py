from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import ContactForm
import re
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def about(request):
    return render(request, "first_app/about.html")

def projects(request):
    return render(request, "first_app/projects.html")

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('first_app/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                contact_email,
                # "Your website" +'',
                ['louis@nuri.codes'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')


    return render(request, 'first_app/contact.html', {'form': form_class})





def test(request):
    response = "Hello I am your first request!"
    return HttpResponse(response)
