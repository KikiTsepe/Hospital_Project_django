"""
This module contains the urls for the 'entities' app.
"""
from django.urls import path
from entities.views.doctor import DoctorListView, DoctorDetailView
from entities.views.nurse import NurseListView, NurseDetailView
from entities.views.patient import PatientListView, PatientDetailView
from entities.views.room import RoomListView, RoomDetailView, RoomDeleteView
from entities.views.homepage import HomepageView

app_name = 'entities'

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("doctors/", DoctorListView.as_view(), name='list_doctor'),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(),
         name='detail_doctor'),
    #  TODO: fix the below views
    path("nurses/", NurseListView.as_view(), name='list_nurse'),
    path("nurses/<int:pk>/", NurseDetailView.as_view(), name='detail_nurse'),
    path("patients/", PatientListView.as_view(), name='list_patient'),
    path("patients/<int:pk>/",
         PatientDetailView.as_view(),
         name='detail_patient'),
    path("rooms/", RoomListView.as_view(), name='list_room'),
    path("rooms/<int:pk>/", RoomDetailView.as_view(), name='detail_room'),
    path("rooms/<int:pk>/", RoomDeleteView.as_view(), name='delete_room'),
]
