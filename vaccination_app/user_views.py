from django.contrib import messages
from django.shortcuts import render, redirect
from vaccination_app.filters import ScheduleFilter
from vaccination_app.forms import ComplaintForm, UserRegister, UserProfileUpdate
from vaccination_app.models import Nurse, User, Hospital, Vaccine, VaccinationSchedule, Complaint, Appointment, \
    ReportCard
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_view')
def user_home(request):
    return render(request, 'usertemplates/home.html')


@login_required(login_url='login_view')
def schedule_user(request):
    s = VaccinationSchedule.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=s)
    s = scheduleFilter.qs
    context = {
        'schedule': s,
        'scheduleFilter': scheduleFilter,
    }
    return render(request, 'usertemplates/schedule.html', context)


@login_required(login_url='login_view')
def take_appointment(request, id):
    schedule = VaccinationSchedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('schedule_user')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointments')
    return render(request, 'usertemplates/take_appointment.html', {'schedule': schedule})


@login_required(login_url='login_view')
def appointments(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'usertemplates/appointments.html', {'appointment': a})


@login_required(login_url='login_view')
def complaint_add_user(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('complaint_user')
    else:
        form = ComplaintForm()
    return render(request, 'usertemplates/complaint_add.html', {'form': form})


@login_required(login_url='login_view')
def complaint_user(request):
    n = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemplates/complaint.html', {'complaint': n})


@login_required(login_url='login_view')
def user_profile(request):
    u = request.user
    profile = User.objects.filter(user=u)
    return render(request, 'usertemplates/user_profile.html', {'profile': profile})


@login_required(login_url='login_view')
def profile_update(request, user_id):
    profile = User.objects.get(user_id=user_id)

    if request.method == 'POST':
        form = UserProfileUpdate(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile Updated Successfully')
            return redirect('user_profile')
    else:
        form = UserProfileUpdate(instance=profile)

    return render(request, 'usertemplates/profile_update.html', {'form': form})


@login_required(login_url='login_view')
def reportcard_user(request):
    u = User.objects.get(user=request.user)
    a = ReportCard.objects.filter(patient=u)
    return render(request, 'usertemplates/report_card.html', {'card': a})
