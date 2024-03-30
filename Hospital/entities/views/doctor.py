"""
This module contains the views of the entities app.
"""
from django.db.models import Count, Avg
from django_filters.views import FilterView
from django.views.generic import DetailView
from entities.models import Doctor, Patient
from entities.filters.doctor import DoctorFilter


class DoctorListView(FilterView):
    model = Doctor
    queryset = Doctor.objects.annotate(num_patients=Count('patient')).all()
    filterset_class = DoctorFilter
    context_object_name = 'context'
    template_name = 'content/doctor/list/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = context.pop("context")
        context["context"] = {
            "filter":
            self.filterset_class,
            "doctors":
            doctors,
            "total_doctors":
            self.object_list.count(),
            "average_salary":
            (self.object_list.aggregate(avg_salary=Avg('salary'))['avg_salary']
             or 0),
            "average_doctor_patients": (self.object_list.aggregate(
                avg_patient=Avg('num_patients'))['avg_patient'] or 0),
            "average_experience": (self.object_list.aggregate(
                avg_experience=Avg('experience'))['avg_experience'] or 0)
        }

        return context


class DoctorDetailView(DetailView):
    model = Doctor
    context_object_name = 'context'
    template_name = 'content/doctor/detail/index.html'

    def get_context_data(self, **kwargs):
        context = super(DoctorDetailView, self).get_context_data(**kwargs)
        doctor = context.pop("context")
        context["context"] = {
            "doctor": doctor,
            "patients": Patient.objects.filter(doctor=doctor)
        }

        return context
