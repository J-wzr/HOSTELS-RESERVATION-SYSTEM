from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.
class UserRole(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    gender_choices = [('M',"Male"),('F',"Female")]
    role = models.OneToOneField(UserRole, on_delete=models.CASCADE, null =True)
    std_name = models.CharField(max_length=30)
    std_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField()
    contact = models.IntegerField()
    district = models.CharField(max_length=30)

    def __str__(self):
        return self.std_name
    
class HostelOwnerRequest(models.Model):
    Name = models.CharField(max_length=30)
    Contact = models.IntegerField()
    Email = models.EmailField()
    Hostel_Name = models.CharField(max_length=30)
    Total_Number_of_Rooms  = models.IntegerField()

    def __str__(self):
        return f"{self.Name} has requested for approval of his/her hostel"
    
class HostelOwner(models.Model):
    landlord_name = models.CharField(max_length=30)
    hostel_name = models.CharField(max_length=30)
    contact = models.IntegerField()

    def __str__(self):
        return self.landlord_name
    

class Hostel(models.Model):
    hostelstat = [("Mixed","Mixed"), ("Single", "Single")]
    waterstatus = [("Tap Water","National Water"), ("Tanks","Only Tanks"),("all", "National water & Tanks")]
    powerstatus = [("full","Power Available"),("solar","Only Solar power"),("all","Power and Solar")]
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=30)
    total_rooms = models.IntegerField()
    Location = models.CharField(max_length=100,)
    lease = models.IntegerField()
    water_status = models.CharField(choices=waterstatus, max_length=10)
    power_status = models.CharField(max_length=100)
    status = models.CharField(choices=hostelstat, max_length=100)
    security_status = models.CharField(max_length=100)
    sop_status = models.CharField(default="Available", max_length=20)
    hostel_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel_owner_contact = models.IntegerField()

    

    def __str__(self):
        return f"Hostel_Name: {self.name} Owner: {self.hostel_owner} "
    
class Booking(models.Model):
    active_contact = models.CharField(max_length=13)
    FirstName = models.CharField(max_length=10, null=False)
    time = models.DateTimeField(auto_now_add=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)


    def __str__(self):
        return f" the number {self.active_contact} booked {self.hostel}" 
