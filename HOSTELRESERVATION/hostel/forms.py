from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
    std_number = forms.IntegerField(required=False)
    class Meta:
        model = Student
        fields = ("std_name", "std_number", "gender", "email", "contact", "district")
        labels = {"std_name":"Student's Name", 
                  "std_number":"Student Number",
                   "gender": "Gender", 
                   "contact": "Contact",
                    "district": "District of Origin"
                }
        

class UserCredentialsForm(UserCreationForm):
    userchoices = [('default_role',"Student"),]
    role = forms.ChoiceField(choices=userchoices)
    class Meta:
        model = User
        fields = ["role","username", "password1", "password2"]

class HostelsForm(forms.ModelForm):
    hostel_owner = forms.ModelChoiceField(queryset=User.objects.filter(first_name='owner'))
    class Meta:
        model = Hostel
        fields = ("__all__")
        labels = {"id":"Hostel id",
                  "status":"Hostel Status",
                  "lease":"Fees Per Semester",
                  "Location": "Location",
                  "total_rooms":"Number of Rooms",
                  "water_status":"Status of Water",
                  "power_status":"Status of Power",
                  "security_status":"Security Status",
                  "sop_status":"SOP's status",
                  "hostel_owner": "Contact person",
                  "hostel_owner_contact":"Contacts"
                  }
        
class HORForm(forms.ModelForm):
    Email = forms.EmailField(required=False)
    class Meta:
        model = HostelOwnerRequest
        fields = "__all__"


class HostelOwnersForm(forms.ModelForm):
    class Meta:
        model = HostelOwner
        fields = ("__all__")

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ("__all__")
