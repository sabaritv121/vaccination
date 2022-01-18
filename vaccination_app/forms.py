import datetime
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from vaccination_app.models import Login, Nurse, Hospital, Vaccine, VaccinationSchedule, Complaint, User, ReportCard


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class NurseRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())

    class Meta:
        model = Nurse
        fields = ('name', 'contact_no', 'email', 'address', 'hospital')


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class UserRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    child_gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ('name', 'contact_no', 'address', 'child_name', 'child_age', 'child_gender')


class HostpitalForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Hospital
        fields = ('name', 'place', 'contact_no', 'email')


class VaccineAdd(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('vaccine_name', 'vaccine_type', 'description')


class ScheduleAdd(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = VaccinationSchedule
        fields = ('hospital', 'date', 'start_time', 'end_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")
        date = cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("End Time should be greater than start Time.")

        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data


class ComplaintForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('subject', 'complaint', 'date')

    def clean_date(self):
        date = self.cleaned_data['date']

        if date != datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date


class UserProfileUpdate(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    child_gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ('name', 'contact_no', 'address', 'child_name', 'child_age', 'child_gender', 'recent_vaccinations')


class AddReportCard(forms.ModelForm):
    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.filter(approval_status=1))

    class Meta:
        model = ReportCard
        fields = ('patient', 'vaccine')
