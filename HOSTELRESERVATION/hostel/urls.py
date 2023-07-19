from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django import views


urlpatterns = [
    path('',HomeView, name="home"),
    path('register/', RegisterView, name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('add-user/', UserCredentials, name="add-user"),
    path('student/', StudentProfile, name="students_profile"),
    path('dean/', DeansProfile, name="deans_profile"),
    path('hostel-owner/', LandlordsProfile, name="landlords_profile"),
    path('owner-request/',HORequest, name="hostel_owner_registration"),
]