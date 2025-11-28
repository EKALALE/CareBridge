from django.shortcuts import render,redirect
from  careapp.models import  *

# Create your views here.
def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')


def appoint(request):
    if request.method == "POST":
        myappointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointment.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')