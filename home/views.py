from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contact(request):
    return render(request,"contact.html")
def booking(request):
    return render(request,"booking.html")
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
    return render(request,"department.html")
