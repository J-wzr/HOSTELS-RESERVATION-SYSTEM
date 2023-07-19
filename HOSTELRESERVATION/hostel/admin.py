from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(UserRole)
admin.site.register(Student)
admin.site.register(Hostel)
admin.site.register(HostelOwner)
admin.site.register(HostelOwnerRequest)
admin.site.register(Booking)