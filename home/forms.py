from django import forms
from .models import Booking

class Calender(forms.DateInput):
    input_type='date'


class Bookingform(forms.ModelForm):
    class Meta:
        model =Booking
        fields='__all__'

        widgets={
            'booking_date':Calender(),
        }

        labels={
           "p_name":"Patient Name",
           "p_phone":"Patient Phone Number",
           "p_email":"Patient Email",
           "doc_name":"Doctor Name",
           "booking_date":"Booking Date",
           "booked_on":"Booked On"

        }
