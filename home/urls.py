
from django.urls import path
from . import views
urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('',views.index,name='index'),
    path('department',views.department,name='department')



]