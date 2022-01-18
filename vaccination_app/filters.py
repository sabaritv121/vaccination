import django_filters
from django import forms
from django_filters import CharFilter, filters
from vaccination_app.models import User, Nurse, Hospital, Vaccine, Appointment


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
                  'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name',)


class NurseFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
                  'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = Nurse
        fields = ('name',)


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
                             'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = Hospital
        fields = ('name',)


class VaccineFilter(django_filters.FilterSet):
    vaccine_name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Search Vaccine Name', 'class': 'form-control'}))

    class Meta:
        model = Vaccine
        fields = ('vaccine_name',)


class PlaceFilter(django_filters.FilterSet):
    schedule__hospital = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Hospital', 'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = ('schedule__hospital',)


class ScheduleFilter(django_filters.FilterSet):
    hospital__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Hospital', 'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = ('hospital__name',)
