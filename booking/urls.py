from django.urls import path
from . import views

urlpatterns = [
    path('Appointment/', views.booking),

]