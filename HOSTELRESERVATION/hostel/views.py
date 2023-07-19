from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import HostelOwnerRequest as HOR
# Create your views here.

def HomeView(request):
    return render(request,"index.html")

def RegisterView(request):    
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are one step away from becoming a valid user. Kindly set your password.")
            return redirect("add-user")
    else:
        form = RegisterForm()
    
    horform = HORForm()
    
    return render(request, "register.html", {"form": form, "horform": horform})

def HORequest(request):
    if request.method == "POST":
        form = HORForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for sending your request for approval of your hostel. We will get back to you soon.")
            return redirect("home")
    else:
        form = HORForm()
    
    register_form = RegisterForm()
    
    return render(request, "owner_request.html", {"form": register_form, "horform": form})




def UserCredentials(request):
    if request.method == "POST":
        form = UserCredentialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCredentialsForm()
    return render(request, "set_credentials.html", {"form": form})

@login_required
def DeansProfile(request):
    if request.method =="POST":
        hostel_owner_form = HostelOwnersForm(request.POST)
        if hostel_owner_form.is_valid():
            hostel_owner_form.save()
        else:
            return HttpResponseRedirect("failed.............")
        return redirect("deans_profile")
    hostel_owner_form = HostelOwnersForm()

    if request.method == "POST":
        hostels_form = HostelsForm(request.POST)
        if hostels_form.is_valid():
            hostels_form.save()
        return redirect("deans_profile")
    hostels_form = HostelsForm()
    hostels = Hostel.objects.all()
    hostel_owners_requests = HOR.objects.all()
    return render(request, "dn_profile.html",{"hostels_form":hostels_form, "hostel_owners_form":hostel_owner_form,"hostel_owners_requests":hostel_owners_requests,"hostels":hostels})

@login_required
def LandlordsProfile(request):
    user = request.user
    hostels = Hostel.objects.filter()
    bookings = Booking.objects.all()
    
    return render(request, 'hostel_owner.html', {'hostels': hostels,"bookings":bookings})



class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.first_name == '':
            return reverse_lazy('students_profile')
        elif self.request.user.first_name=="owner":
            return reverse_lazy('landlords_profile')
        else:
            return reverse_lazy('deans_profile')

        
@login_required       
def StudentProfile(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=True)
            booking.save()
            messages.success(request, 'Booking successful! Please wait for approval.')
            return redirect('students_profile')
    else:
        form = BookingForm()
    hostels = Hostel.objects.all()
    return render(request, "std_profile.html",{"hostels":hostels,"bookingform":form})
