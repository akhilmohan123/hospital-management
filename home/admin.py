from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Departments)
admin.site.register(models.Doctors)
class Bookingtuple(admin.ModelAdmin):
    model=models.Booking
    list_tuple=("p name","p phone","p email","doc name","booking date","booked on")

admin.site.register(models.Booking,Bookingtuple)