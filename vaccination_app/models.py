from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}, {self.place}"


class Nurse(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    child_name = models.CharField(max_length=100)
    child_age = models.CharField(max_length=100)
    child_gender = models.CharField(max_length=100)
    recent_vaccinations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=200)
    vaccine_type = models.CharField(max_length=200)
    description = models.TextField()
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.vaccine_name


class VaccinationSchedule(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(VaccinationSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, null=True, blank=True)
    vaccinated = models.BooleanField(default=False)


class ReportCard(models.Model):
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING)
