from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("patient", views.patient, name="patient"),
    path("historyform/<int:patient_id>", views.history, name="history"), # create a new form for a patient
    path("file/<int:patient_id>", views.file, name="file"), #pull a patien file
    path("fileview/<int:file_id>", views.fileview, name="fileview"),
    path("delete/<int:file_id>/<int:patient_id>", views.delete, name="deletefile"),
    path("appointments", views.appointments, name="appointments"),

    # API routes
    path("patients", views.patients, name="patients"),
    path("search/<str:input>", views.search, name="search"),
    path("edit/<int:id>", views.edit, name="edit"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)