# Anamnesis Application

## About Anamnesis and The Reason for Building It
My project was born from my observation that many medicial clinics in Guatemala use either paper files or impractical technology to keep track of their patients' medical history. Furthermore, the use of weekly paper agendas to organize appointments is very common.<br><br>
Due to the nature of my project, I called it *medomai* which is the Greek word for 'to think of' or 'be mindful of' and relates to the modern term 'medicine.' The app, in turn, is called *anamnesis*, which in medical jargon means 'patient's history'. This name was given becasuse one of the main features of the app is to manage patients' history.<br><br>
The purpose of the project is to provide doctors a managing tool that is easy to use. This tool will allow them to be more time efficient, organized, and have easy access to their patient's data.

## Distinctiveness and Complexity
The projects completed for CS50's Web programming built one after another in complexity, but not in purpose. Furthermore, UI was not of primary importance, even tho the use of frameworks such as Bootstrap and CSS was encouraged. In this sense, Anamnesis is distinct from the projects required for the course in purpose, complexity and UI.<br>

The purpose of the app is to allow medical doctors to manage a database of their patients from any device, whether it is a computer or a mobile device; therefore, keeping in a non-destructive way the information of patients. The app is designed specifically for medical doctors in the context of Guatemala. That is evident in the way a patient is added to the database where the states of the country are given a priori in the form.<br>

As opposed to the social media project, where the aim was the interaction between users and posting information, Anamnesis builds a patient's file with multiple *anamnesis* (medical history) using two Django models, one for the patient and one for the medical records of the patient. A User model is added with the intention that the app holds multiple doctor users, each one with their individual database of their patients. That is to say, one doctor cannot access the data of another doctor user.<br>

The complexity of the app comes to play in the way a doctor user can create, retrieve, update and keep track of their patients' medical records. There is only one url `patient/` for creating and querying in the database. In this url, an html page displays three things: a *see all patients* link that queries and displays all patients of the logged-in doctor user; a *search* form where you can look up a patient by name, last name or typing a few characters; and a *create a new patient* form that allows the user to create a new patient file. Except for creating a new patient, seeing all patients and searching work via APIs and JavaScript so that the server is hit only once for different operations.<br>

Different urls are used for various operations such as viewing a patient's file, which may contain one or multiple medical records; pulling a specific medical record to examine; deleting a medical record; creating a patient and a patient's record. A third API `edit/<int:id>` allows via JavaScript to edit a patient's medical history.

The complexity of the app ends with the appointments feature. This feature via `appointments/`route queries the appointments assigned to the patients. They are display in an html `appointments.html` in alphabetical order and by date. 

In terms of the UI, a specific scheme color was chosen to give the app an identity to the app; a single route for various operations allow the user easy accesibility to the main features of the app. Furthermore, mobile responsiveness gives flexibility in terms of access.

## Structure
The project name is Medomai, which is the main directory. An app was created using Django named Anamnesis. Under the app, there are several files. For practical purposes, a static folder was created in which there is a folder named *anamnesis*. In this folder there are three other items: a folder named images with the purpose of organizing all the images to be used in the app; the *log.js* file contains the JavaScript code for the application--in most cases APIs are used in this file. A *styles.css* contains the styling and presentation of the app.

In folder named *templates*, another folder was created which contains all the html files used in the application. In alphabetical order, *appointments.html* contains the markup for displaying the list of appointments a user doctor is expecting during the day and in the future. *Fileview.html* displays a single history record of a patient with the reason for the visit of the patient, the history of illness, the diagnostic, the prescription and a date for the next appointment. Via JavaScript, this file can be edited. *index.html* is the main page filled with information and a few instructions on how to use the app. *Layout.html* is the skeleton of the app where all the `<scripts>`are loaded and a nav bar is constructed to be displayed at all times. *Login.html and register.html* are the places where a doctor can log in if he possesses credentials or get registered otherwise. 

The next three files represent main funciontalities of the app. *PatientFile.html* is the main file of each patient. It is filled via a function with the different medical records of the patient. Via this interface, the user can click to view a specific record or delete it. *PatientHistory.html* is a form the doctor can fill in to create a new medical record for a patient with the reason for the visit, the history of the illness, the diagnosis, the prescription and the date for the next appointment. 
 
Finally, *patients.html* contains the main part of the app with a link to see all patients, a search bar and a form to create a new patient.

A *urls.py* was created with all the routes that form the logic of the app along with the file *views.py*. Both files form the back-end of the application and the mechanics sort of speak of it.

## How to run the application
First, install the library *pytz* listed in the file *requirements.txt* found in the main directory. Run `python manage.py runserver`. Once the app is running, create a user and log in. When you click the *patients* tab in the navbar, you will be able to create a new patient, search for a patient or list all your patients. When you create a new patient, once the form is submitted, it will redirect you to an form to create the first *anamnesis* (a patient's record) of the new patient. 

If you search for a patient recently created, or list your patients, you are able to click on the name and it will direct you to the file of the patient which can contain a single or multiple records. On the file of the patient, you are able to view single records or delete them. If you decide to view a record, it will direct you inside the record where you will be able to edit it. Clickin on the name of the patient will always direct you to the patient's main file.

Once you assign appointments to your patients, you can go to the *appointments* tab on the navbar. An interface will display with a list of the appointments of your patients, organized by date. No appointment older than today will be shown. To look for a past appointment, search for the patient file. 

If you want to see a demostration of the app via YouTube, click on the following link [Demostration](https://youtu.be/bCvxh6AMhtk).

