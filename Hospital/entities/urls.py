from django.urls  import path
from entities.views.doctor import DoctorListView

app_name = 'entities'

urlpatterns = [
    path("list_doctor/",DoctorListView.as_view(),name = 'list_doctor'),
]