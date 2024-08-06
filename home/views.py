from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments,Doctors
from .forms import Bookingform
# Create your views here.
def contact(request):
    return render(request,"contact.html")
def booking(request):
    if request.POST:
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"confirmation.html")
    form=Bookingform()
    data={
       'form': form
    }
    return render(request,"booking.html",data)
def doctors(request):
    return render(request,"doctor.html")
def about(request):
    return render(request,"about.html")
def index(request):
    person={
        "name":"akhil",
        "age":20,
        "place":"thrissur"
    }
    return render(request,"index.html",person)
def department(request):
    departments={
        'dept':Departments.objects.all()
    }

    return render(request,"department.html",departments)
def doctors(request):
    doct={
        "d":Doctors.objects.all()
    }
    return render(request,"doctor.html",doct)
