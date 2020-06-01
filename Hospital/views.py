from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserLoginForm, UserRegistrationForm, PatientForm, PrescriptionForm, AppointmentForm, DoctorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import *
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

def home(request):
    return render(request, 'Hospital/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patient(request):
    patient = request.user.patient
    appointment = patient.appointment_set.all()
    context = {
        'appointment': appointment
    }
    return render(request, 'Hospital/patient_appointment.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patientProfile(request):
    patient = request.user.patient
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'Hospital/patient_profile.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patientMedicalHistory(request):
    patient = request.user.patient
    prescription = patient.prescription_set.all()
    context = {
        'prescription': prescription
    }
    return render(request, 'Hospital/patientMedicalHistory.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def doctorAppointment(request):
    doctor = request.user.doctor
    appointment = doctor.appointment_set.all()
    context = {
        'appointment': appointment
    }
    return render(request, 'Hospital/doctor_appointment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def doctorPrescription(request):
    doctor = request.user.doctor
    prescription = doctor.prescription_set.all()
    context = {
        'prescription': prescription
    }
    return render(request, 'Hospital/prescription.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def createPrescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription')

    context = {
        'form': form
    }

    return render(request, 'Hospital/createPrescription.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Receptionist'])
def allAppointment(request):
    appointment = Appointment.objects.all()
    patient = Patient.objects.all()
    total_appointment = appointment.count()
    appointment_done = appointment.filter(status='Approved').count()
    appointment_pending = appointment.filter(status='Pending').count()

    context = {
        'total_appointment': total_appointment,
        'appointment_done': appointment_done,
        'appointment_pending': appointment_pending,
        'appointment': appointment,
        'patient': patient,
    }

    return render(request, 'Hospital/allAppointment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Receptionist'])
def newAppointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'Hospital/newAppointment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Receptionist'])
def createPatient(request):
    form = PatientForm()
    
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {
        'form': form
    }
    return render(request, 'Hospital/patient_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Receptionist'])
def deletePatient(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('/dashboard')
    
    context = {
        'patient': patient
    }
    return render(request, 'Hospital/deletepatient.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Receptionist'])
def updatePatient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {
        'form': form
    }
    return render(request, 'Hospital/patient_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HR'])
def hrDashboard(request):
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    total_doctor = doctor.count()
    total_patient = patient.count()
    active_doctor = doctor.filter(status='Active').count()
    
    context = {
        'total_doctor': total_doctor,
        'total_patient': total_patient,
        'active_doctor':active_doctor,
        'doctor': doctor
    }
    return render(request, 'Hospital/hrdashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HR'])
def updateDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/hr')

    context = {
        'form': form
    }
    return render(request, 'Hospital/doctor_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HR'])
def deleteDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('/hr')
    
    context = {
        'doctor': doctor
    }
    return render(request, 'Hospital/deletedoctor.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HR'])
def allAccount(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient,
    }
    return render(request, 'Hospital/allaccount.html', context)


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Welcome {user}')
                    return redirect('home')
                else:
                    messages.warning(request, 'No active user')
            else:
                messages.warning(request, 'Invalid Username or Password')
    else:
        form = UserLoginForm()
    context = {
            'form': form,
        }
    return render(request, 'account/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login')

@unauthenticated_user
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            username = form.cleaned_data.get('username')
            user = form.save()
            messages.success(request, 'You have successfully registered. Please login')
            return redirect('/login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)