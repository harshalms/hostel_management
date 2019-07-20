from django.shortcuts import render
from django.http import HttpResponse
import os
from hostelapp.models import Hostel
from hostelapp.models import Student
from hostelapp.models import Room
from hostelapp.models import Staff
from hostelapp.models import Mess
from hostelapp.models import StudentRoom

# Create your views here.

def hello(request):
    text = """<h>Welcome to my Hostel app !</h1>"""
    return HttpResponse(text)

def hostel(request):
    objects=Hostel.objects.all()
    house=[]
    for i in objects:
        house.append({
            'name': i.hostel_name,
            'rooms': i.total_rooms,
            'add': i.address,
            'created': i.created_on,
            'updated': i.updated_on
        })
    print(house)
    return render(request, '.html', {'data': house})

def student(request):
    objects=Student.objects.all()
    pupil=[]
    for i in objects:
        pupil.append({
            'name': i.name,
            'roll': i.roll_no,
            'mail': i.email,
            'contact': i.phone,
            'created': i.created_on,
            'updated': i.updated_on
        })
    print(pupil)
    return render(request, '.html', {'data1':pupil})


def mess(request):
    objects=Mess.objects.all()
    food=[]
    for i in objects:
        food.append({
            'name': i.mess_name,
            'created': i.created_on,
            'updated': i.updated_on
        })
