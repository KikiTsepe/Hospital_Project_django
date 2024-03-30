"""
This module contains the urls for the 'entities' app.
"""
from django.urls import path
from entities.views.doctor import DoctorListView, DoctorDetailView
from entities.views.homepage import HomepageView

app_name = 'entities'

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("doctors/", DoctorListView.as_view(), name='list_doctor'),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(),
         name='detail_doctor'),
    #  TODO: fix the below views
    path("nurses/", DoctorListView.as_view(), name='list_nurse'),
    path("patients/", DoctorListView.as_view(), name='list_patient'),
    path("rooms/", DoctorListView.as_view(), name='list_room'),
    path("patients/<int:pk>/",
         DoctorDetailView.as_view(),
         name='detail_patient'),
]
