from django.contrib import messages
from django.shortcuts import render, redirect
from vaccination_app.filters import NurseFilter, UserFilter, HospitalFilter, VaccineFilter, PlaceFilter
from vaccination_app.forms import NurseRegister, UserRegister, HostpitalForm, VaccineAdd, AddReportCard
from vaccination_app.models import Nurse, User, Hospital, Vaccine, Complaint, Appointment, ReportCard
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_view')
def admin_home(request):
    return render(request, 'admintemp/home.html')


@login_required(login_url='login_view')
def nurse(request):
    n = Nurse.objects.all()
    nurseFilter = NurseFilter(request.GET, queryset=n)
    n = nurseFilter.qs
    context = {
        'nurse': n,
        'nurseFilter': nurseFilter,
    }
    return render(request, 'admintemp/nurse.html', context)


@login_required(login_url='login_view')
def nurse_update(request, user_id):
    n = Nurse.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = NurseRegister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('nurse')
    else:
        form = NurseRegister(request.POST or None, instance=n)
    return render(request, 'admintemp/nurse_update.html', {'form': form})


@login_required(login_url='login_view')
def nurse_delete(request, user_id):
    n = Nurse.objects.get(user_id=user_id)
    if request.method == 'POST':
        n.delete()
        return redirect('nurse')
    else:
        return redirect('nurse')


@login_required(login_url='login_view')
def user_view(request):
    n = User.objects.all()
    userFilter = UserFilter(request.GET, queryset=n)
    n = userFilter.qs
    context = {
        'user': n,
        'userFilter': userFilter,
    }
    return render(request, 'admintemp/user.html', context)


@login_required(login_url='login_view')
def user_update(request, user_id):
    n = User.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = UserRegister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('user_view')
    else:
        form = UserRegister(instance=n)
    return render(request, 'admintemp/user_update.html', {'form': form})


@login_required(login_url='login_view')
def user_delete(request, user_id):
    n = User.objects.get(user_id=user_id)
    if request.method == 'POST':
        n.delete()
        return redirect('user_view')
    else:
        return redirect('user_view')


@login_required(login_url='login_view')
def add_hospital(request):
    form = HostpitalForm()
    if request.method == 'POST':
        form = HostpitalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Hospital Added Successfully')
            return redirect('hospital')
    else:
        form = HostpitalForm()
    return render(request, 'admintemp/hospital_add.html', {'form': form})


@login_required(login_url='login_view')
def hospital(request):
    n = Hospital.objects.all()
    hospitalFilter = HospitalFilter(request.GET, queryset=n)
    n = hospitalFilter.qs
    context = {
        'hospital': n,
        'hospitalFilter': hospitalFilter,
    }
    return render(request, 'admintemp/hospital.html', context)


@login_required(login_url='login_view')
def hospital_update(request, id):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        form = HostpitalForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, 'Hospital Updated Successfully')
            return redirect('hospital')
    else:
        form = HostpitalForm(instance=n)
    return render(request, 'admintemp/hospital_update.html', {'form': form})


@login_required(login_url='login_view')
def hospital_delete(request, id):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Hospital Deleted Successfully')
        return redirect('hospital')
    else:
        return redirect('hospital')


@login_required(login_url='login_view')
def add_vaccine(request):
    form = VaccineAdd()
    if request.method == 'POST':
        form = VaccineAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Vaccine Added Successfully')
            return redirect('vaccine')
    else:
        form = VaccineAdd()
    return render(request, 'admintemp/vaccine_add.html', {'form': form})


@login_required(login_url='login_view')
def vaccine(request):
    n = Vaccine.objects.all()
    vaccineFilter = VaccineFilter(request.GET, queryset=n)
    n = vaccineFilter.qs
    context = {
        'vaccine': n,
        'vaccineFilter': vaccineFilter,
    }
    return render(request, 'admintemp/vaccine.html', context)


@login_required(login_url='login_view')
def vaccine_update(request, id):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = VaccineAdd(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, 'Vaccine Updated Successfully')
            return redirect('vaccine')
    else:
        form = VaccineAdd(instance=n)
    return render(request, 'admintemp/vaccine_update.html', {'form': form})


@login_required(login_url='login_view')
def vaccine_delete(request, id):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Vaccine Deleted Successfully')
        return redirect('vaccine')
    else:
        return redirect('vaccine')


@login_required(login_url='login_view')
def vaccine_approve(request, id):
    n = Vaccine.objects.get(id=id)
    n.approval_status = 1
    n.save()
    messages.info(request, 'Vaccine Approved Successfully')
    return redirect('vaccine')


@login_required(login_url='login_view')
def vaccine_reject(request, id):
    n = Vaccine.objects.get(id=id)
    n.approval_status = 2
    n.save()
    messages.info(request, 'Vaccine Rejected Successfully')
    return redirect('vaccine')


@login_required(login_url='login_view')
def complaint_admin(request):
    n = Complaint.objects.all()
    return render(request, 'admintemp/complaint.html', {'complaint': n})


@login_required(login_url='login_view')
def reply_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('complaint_admin')
    return render(request, 'admintemp/reply_complaint.html', {'complaint': complaint})


@login_required(login_url='login_view')
def appointment_admin(request):
    n = Appointment.objects.all()
    placeFilter = PlaceFilter(request.GET, queryset=n)
    n = placeFilter.qs
    context = {
        'appointment': n,
        'placeFilter': placeFilter,
    }
    return render(request, 'admintemp/appointments.html', context)


@login_required(login_url='login_view')
def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def vaccinated_list(request):
    a = Appointment.objects.filter(status=1).order_by('schedule__hospital')
    return render(request, 'admintemp/vaccinated.html', {'appointment': a})


@login_required(login_url='login_view')
def add_reportcard(request):
    form = AddReportCard()
    if request.method == 'POST':
        form = AddReportCard(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Report Card Added Successfully')
            return redirect('report_card')
    else:
        form = AddReportCard()
    return render(request, 'admintemp/reportcard_add.html', {'form': form})


@login_required(login_url='login_view')
def report_card(request):
    a = ReportCard.objects.all()
    return render(request, 'admintemp/report_card.html', {'card': a})
