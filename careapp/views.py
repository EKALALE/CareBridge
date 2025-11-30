from django.shortcuts import render, redirect, get_object_or_404
from careapp.models import Appointment
from django.contrib import messages


# Home pages
def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


# Show appointments
def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html', {"all": all})


# Delete appointment
def delete(request, id):
    myappoint = get_object_or_404(Appointment, id=id)
    myappoint.delete()
    messages.success(request, 'Appointment deleted successfully!')
    return redirect('/show')


# Create new appointment
def appoint(request):
    if request.method == "POST":
        myappointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],  # FIXED
            doctor=request.POST['doctor'],  # FIXED
            message=request.POST['message'],
        )
        myappointment.save()

        messages.success(request, 'Your Appointment has been successfully booked!')
        return redirect('/appointment')

    return render(request, 'appointment.html')


# Edit appointment
def edit(request, id):
    editappointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.datetime = request.POST.get('date')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')  # FIXED
        editappointment.message = request.POST.get('message')

        editappointment.save()
        messages.success(request, 'Your appointment has been updated successfully!')

        return redirect('/show')  # FIXED redirect

    return render(request, 'edit.html', {'editappointment': editappointment})
