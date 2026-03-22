from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from . models import Project , Technology , Contacter , Message , Service , MyPhoneNumber , MyEmail
import smtplib
from utils import email_service
import os
from django.contrib import messages

curr_dir = os.getcwd()
print(curr_dir)
# Create your views here.
def home(request):
    phone_number = MyPhoneNumber.objects.all().first()
    email_address = MyEmail.objects.all().first()
    return render(request , "portfolio/index.html",{
        "phone_number": phone_number ,
        "email_address": email_address  
    })

def services(request):
    services = Service.objects.all()
    return render(request , "portfolio/services.html" ,
    {
        "services": services
    }
    )

def projects(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    return render(request , "portfolio/projects.html",{
        "projects": projects, 
        "technologies": technologies 
    })

def resume(request):
    return render(request , "portfolio/resume.html")

def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get("name")
        contact_email = request.POST.get("email")
        contact_message = request.POST.get("message")

        #Send email to the user
        
        #Create a Contacter instance in the DB
        #Check whether the email doesn't exist in the DB 
        try:
            contacter = get_object_or_404( Contacter , email = contact_email )
            message = Message.objects.create(
                contacter = contacter ,
                content = contact_message
            )
        except Exception as e:
            contacter = Contacter.objects.create(
                name = contact_name ,
                email = contact_email
            )
            message = Message.objects.create(
                contacter = contacter ,
                content = contact_message
            )

      #SEND EMAIL TO THE CONTACTER
        try:   
            email_service.send_email( receiver_email = contact_email , receiver_name = contact_name )
           # email_service.sendmail()
            messages.info(request , "Your message has been received. Check your email's inbox.")
        except Exception as e:
            messages.error(request , f"Error: {e}")
        
        #SEND EMAIL TO THE DEVELOPER
        email_service.notify_developer()
        return redirect("contact")
    #If the redirection is comming from submitted form
    return render(request , "portfolio/contact.html",{
        "messages": messages,
        #"latest_message": latest_message , 
       # "messages_exists": messages_exists
    })

def faqs(request):
    return render(request , "portfolio/faqs.html")  