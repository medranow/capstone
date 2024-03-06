from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User
from datetime import datetime
from django.db import IntegrityError
from django.http import JsonResponse
from django.core import serializers
import json
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import pytz

# Import my models
from .models import Patient, Patienthistory

# Create your views here.
def index(request):
    doctor = request.user.get_username()
    return render(request, "anamnesis/index.html", {
        'doctor': doctor,
    })

# Log in user
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "anamnesis/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "anamnesis/login.html")

# Logout user    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register user = doctor
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"] 

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "anamnesis/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "anamnesis/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "anamnesis/register.html")

# create and see a new patient
def patient(request):
    if request.method == "GET":   
        return render(request, "anamnesis/patients.html")
    
    
    if request.method == "POST":
        # Get the information to create a new patient
        doctor = request.user
        name = request.POST["name"]
        lastname = request.POST["lastname"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        phone = request.POST["phonenumber"]

        
        # Create a new patient
        newPatient = Patient (
            doctor =doctor,
            name = name,
            lastname = lastname,
            address = address,
            city = city,
            state = state,
            phonenumber = phone,
            date = datetime.now()
        )
        newPatient.save()

        # Get the id of new patient just created
        patient_id = Patient.objects.get(pk=newPatient.id)

        # Redirect the user to the form of the patient
        
        return HttpResponseRedirect(reverse("history", args=(patient_id.id,)))

# Render an anamnesis for the patient just created
def history(request, patient_id):
    if request.method == "GET":
        #Get the patient whose id was provided
        patient = Patient.objects.get(pk=patient_id)
        name = patient.name
        lastname = patient.lastname
        date = patient.date
        patientid = patient.id
        return render(request, "anamnesis/patientHistory.html", {
            "name": name.capitalize(),
            "lastname": lastname,
            "date": date,
            "patientid": patientid

        })
    return render(request, "f'anamnesis/historyForm/{patientid}")
    
    

# Show the patient file
def file(request, patient_id):
    if request.method == "GET":
        patient = Patient.objects.get(pk=patient_id)
        files = Patienthistory.objects.filter(patient_id=patient_id)

        # Pagination
         # Pagination
        paginator = Paginator(files, 10) #show 10 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, "anamnesis/patientFile.html", {
            "patient": patient,
            "files": page_obj,
        })

# if statement to save information of the patient
    if request.method == "POST":

        patient_instance = Patient.objects.get(pk=patient_id)

        reasonforvisit = request.POST["reasonforvisit"]
        historyofillness = request.POST["historyofillness"]
        diagnostic = request.POST["diagnostic"]
        prescription = request.POST["prescription"]
        date = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M') # Convert the input value to a Python datetime object 

        newFile = Patienthistory(
            patient = patient_instance,
            date = datetime.now(),
            diagnostic = diagnostic,
            history = historyofillness,
            prescription = prescription,
            visit = reasonforvisit,
            nextappointment = date,

        )

        newFile.save()

        # Redirect the doctor to the file of the patient
        return HttpResponseRedirect(reverse("file", args=(patient_id,)))


def fileview(request, file_id):
    fileofpatient = Patienthistory.objects.get(pk=file_id)
    return render(request, "anamnesis/fileview.html", {
        "fileofpatient": fileofpatient,
    })

# Delete a file
def delete(request, file_id, patient_id):
    try:
        fileDelete = Patienthistory.objects.get(pk=file_id).delete()
        return HttpResponseRedirect(reverse("file", args=(patient_id,)))
    except Patienthistory.DoesNotExist:
                return render(request, "anamnesis/index.html", {
                    'message': "file does not exist",
                })

# Show appointments
def appointments(request):
    if request.method == "GET":
        appointments = Patienthistory.objects.all().order_by('nextappointment')

        aware_datetime = datetime.now(pytz.utc)  # Create an aware datetime object with timezone information

        listappointments = []
        for appointment in appointments:
            # Check if appointment.nextappointment is not None and is in the future
            if appointment.nextappointment is not None and appointment.nextappointment >= aware_datetime:
                listappointments.append(appointment)

        # Pagination
        paginator = Paginator(listappointments, 10) #show 10 posts per page
        page_number = request.GET.get('page')
        listappointments = paginator.get_page(page_number)

        return render(request, "anamnesis/appointments.html", {
            'appointments': listappointments,
        })


# API functiosn
def edit(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        formToEdit = Patienthistory.objects.get(pk=id)
        formToEdit.diagnostic = data['diagnostic']
        formToEdit.prescription = data['prescription']
        
        # Check if the date is provided in the data
        if 'date' in data and data['date']:
            date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M') # Convert the input value to a Python datetime object 
            formToEdit.nextappointment = date
        else:
            formToEdit.nextappointment = None  # Set nextappointment to None if date is not provided

        formToEdit.save()



        formToEdit.save()
        return JsonResponse({"message": "saved succesfully"})


def patients(request):
    if request.method == "GET":


        patients = Patient.objects.filter(doctor=request.user).order_by('name').values('name', 'lastname', 'id')

        return JsonResponse({'message': 'all patients fetched', "data": list(patients)})

def search(request, input):
    user = request.user

    if request.method == "GET":
        matches = Patient.objects.filter(name__icontains=input, doctor=user)
        
        if matches:
            return JsonResponse({'message': 'all patients fetched', 'data': list(matches.values())})
        else:
            matches = Patient.objects.filter(lastname__icontains=input, doctor=user)
            return JsonResponse({'message': 'all patients fetched', 'data': list(matches.values())})
