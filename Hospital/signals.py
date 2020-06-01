from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Patient, Doctor

def patient_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='patient')
        instance.groups.add(group)
        Patient.objects.create(user=instance, name=instance.username,)

post_save.connect(patient_profile, sender=User)

# def doctor_profile(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name='doctor')
#         instance.groups.add(group)
#         Doctor.objects.create(user=instance, name=instance.username,)

# post_save.connect(doctor_profile, sender=User)