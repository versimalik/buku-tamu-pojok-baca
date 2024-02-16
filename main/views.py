from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Guest
from django.urls import reverse
from django.core.mail import send_mail
import datetime 

def index(request): 
    return render(request,"main/index.html")

def create(request):
    fullname = request.POST['fullname']
    email = request.POST['email']
    phone = request.POST['phone']
    origin = request.POST['origin']
    current_datetime = datetime.datetime.now()
    guest = Guest (
        fullname = fullname,
        phone = phone,
        email = email,
        origin = origin,
        DateTime = current_datetime
    )
    guest.save()

    send_mail(
        subject="Selamat Datang Di Pojok Baca",
        message=f"Hi {fullname} selamat datang di pojok baca",
        from_email="mega.wibowo21@gmail.com",
        recipient_list=[email]

    )



    return HttpResponseRedirect(reverse("main"))




