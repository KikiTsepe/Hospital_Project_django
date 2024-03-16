from django.shortcuts import render
from django.views.generic import TemplateView
from entities.models import Doctor

class DoctorListView(TemplateView):
    
    template_name = 'doctor/index.html'
