from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    path('patient/profile', views.patientProfile, name='patientProfile'),
    path('patient/medical', views.patientMedicalHistory, name='medical'),
    path('doctor/', views.doctorAppointment, name='appointment'),
    path('doctor/prescription/', views.doctorPrescription, name='prescription'),
    path('doctor/create', views.createPrescription, name='create'),
    path('dashboard/', views.allAppointment, name='dashboard'),
    path('dashboard/newappointment/', views.newAppointment, name='newappointment'),
    path('dashboard/updatepatient/<int:id>', views.updatePatient, name='update'),
    path('dashboard/deletepatient/<int:id>', views.deletePatient, name='delete'),
    path('dashboard/createpatient/', views.createPatient, name='createpatient'),
    path('hr/', views.hrDashboard, name='hr'),
    path('hr/updatedoctor/<int:id>', views.updateDoctor, name='updatedoctor'),
    path('hr/deletedoctor/<int:id>', views.deleteDoctor, name='deletedoctor'),
    path('hr/account/', views.allAccount, name='account'),
]
