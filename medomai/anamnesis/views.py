from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User
from datetime import datetime
from django.db import IntegrityError
from django.http import JsonResponse

# Import my models
from .models import Patient, Patienthistory

# Create your views here.
def index(request):
    return render(request, "anamnesis/index.html")

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
        name = request.POST["name"]
        lastname = request.POST["lastname"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        phone = request.POST["phonenumber"]

        
        # Create a new patient
        newPatient = Patient (
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
    return render(request, "anamnesis/patientHistory.html", {
        "patient_id": patient_id
    })

