from django.contrib import admin
from . models import *

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'id','name'
    ]

class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'id','name'
    ]

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment)
admin.site.register(Prescription)
