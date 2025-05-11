"""
This module contains the nurse views of the entities app.
"""
from typing import Any
from django.db.models import Avg, Count
from django_filters.views import FilterView
from django.views.generic import DetailView
from entities.models import Nurse, Patient
from entities.filters.nurse import NurseFilter


class NurseListView(FilterView):
    model = Nurse
    queryset = Nurse.objects.select_related('room_in_charge').annotate(
        patients_num=Count('room_in_charge__patient'))
    filterset_class = NurseFilter
    context_object_name = "context"
    template_name = "content/nurse/list/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx: dict[str, Any] = super().get_context_data(**kwargs)
        nurses = ctx.pop("context")
        ctx["context"] = {
            "filter":
            self.filterset_class,
            "nurses":
            nurses,
            "total_nurses":
            self.object_list.count(),
            "average_salary":
            (self.object_list.aggregate(avg_salary=Avg("salary"))["avg_salary"]
             or 0),
            "average_experience": (self.object_list.aggregate(
                avg_experience=Avg("experience"))["avg_experience"] or 0)
        }

        return ctx


class NurseDetailView(DetailView):
    model = Nurse
    context_object_name = "context"
    template_name = "content/nurse/detail/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super(NurseDetailView, self).get_context_data(**kwargs)
        nurse = ctx.pop("context")
        ctx["context"] = {
            "nurse": nurse,
            "patients": Patient.objects.filter(room=nurse.room_in_charge)
        }
        return ctx
