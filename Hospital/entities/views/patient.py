"""
This module contains the patient views of the entities app.
"""
from typing import Any
from django.db.models import Avg
from django.views.generic import DetailView
from django_filters.views import FilterView
from entities.models import Patient, Nurse
from entities.filters.patient import PatientFilter


class PatientListView(FilterView):
    model = Patient
    queryset = Patient.objects.all()
    filterset_class = PatientFilter
    context_object_name = "context"
    template_name = "content/patient/list/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx: dict[str, Any] = super().get_context_data(**kwargs)
        patients = ctx.pop("context")
        ctx["context"] = {
            "filter":
            self.filterset_class,
            "patients":
            patients,
            "total_patients":
            self.object_list.count(),
            "average_age":
            (self.object_list.aggregate(avg_age=Avg("age"))["avg_age"] or 0),
        }
        return ctx


class PatientDetailView(DetailView):
    model = Patient
    context_object_name = "context"
    template_name = "content/patient/detail/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super(PatientDetailView, self).get_context_data(**kwargs)
        patient = ctx.pop("context")
        ctx["context"] = {
            "patient": patient,
            "nurses": Nurse.objects.filter(room_in_charge=patient.room)
        }
        return ctx
