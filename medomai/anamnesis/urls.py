from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("patient", views.patient, name="patient"),
    path("historyform/<int:patient_id>", views.history, name="history"),
    path("file/<int:patient_id>", views.file, name="file"), #pull a patien file
    path("fileview/<int:file_id>", views.fileview, name="fileview"),

    # API routes
    path("patients", views.patients, name="patients")

]