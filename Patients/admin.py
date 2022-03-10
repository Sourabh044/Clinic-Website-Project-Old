from django.contrib import admin
from Patients.models import Patients
from .models import Patients
# Register your models here.
admin.site.register(Patients)