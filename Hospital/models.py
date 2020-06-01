from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     U_type = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.user.username

class Doctor(models.Model):
    profile = [
        ('Heart', 'Heart'),
        ('Livour', 'Livour'),
        ('ENT', 'ENT'),
        ('Mind', 'Mind'),
        ('Ortho', 'Ortho'),
    ]
    departments = [
        ('Onchology', 'Onchology'),
        ('Neurology', 'Neurology'),
        ('Ortho', 'Ortho'),
        ('Cardiology', 'Cardiology'),
    ]
    STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]
    gender = [('Male', 'Male'), ('Female', 'Femaile'), ('Other', 'Other')]
    id = models.AutoField(primary_key=True, null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    speciality = models.CharField(max_length=10, choices=profile)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender)
    age = models.PositiveIntegerField(default=0, null=True)
    address = models.TextField(null=True, blank=True)
    department = models.CharField(max_length=20, choices=departments, null=True)
    attandance = models.PositiveIntegerField(default=0, null=True)
    salary = models.PositiveIntegerField(default=0, null=True)
    status = models.CharField(max_length=15, choices=STATUS, null=True)
    

    def __str__(self):
        return self.user.username
      

class Patient(models.Model):
    BLOOD = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B-'),
        ('O+', 'O-'),
        ('AB+', 'AB-')
    ]
    id = models.AutoField(primary_key=True, null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100 , null=True, blank=True)
    Phone = models.CharField(max_length=100 , null=True, blank=True)
    gender = models.CharField(max_length=100 , null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=500 , null=True, blank=True)
    bloodGroup = models.CharField(max_length=5, null=True, blank=True, choices=BLOOD)
    outstanding = models.PositiveIntegerField(default=0)
    paid = models.PositiveIntegerField(default=0)
    casepaper = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor , null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(null=True)
    STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    message = models.CharField(max_length=1000 , default="Pending Approval")

    def __str__(self):
        return str(self.doctor)+"--"+str(self.patient)


class Prescription(models.Model):
    priscription = models.CharField(max_length=500, null=True, blank=True)
    desease = models.CharField(max_length=100, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.desease)+"----"+str(self.patient)
    
