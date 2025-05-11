"""
This module contains the Room views of the entities app.
"""
from typing import Any
from django.urls import reverse_lazy
from django.db.models import Avg, Count, F, Sum
from django.views.generic import DetailView, DeleteView
from django_filters.views import FilterView
from entities.models import Room, Nurse, Patient
from entities.filters.room import RoomFilter


class RoomListView(FilterView):
    model = Room
    queryset = (Room.objects.all().annotate(
        reserved_beds=Count('patient')).annotate(
            free_beds=F('capacity') -
            F('reserved_beds')).annotate(num_nurses=Count('nurse')).annotate(
                num_patients=Count('patient')))
    filterset_class = RoomFilter
    context_object_name = "context"
    template_name = "content/room/list/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx: dict[str, Any] = super().get_context_data(**kwargs)
        rooms = ctx.pop("context")
        ctx["context"] = {
            "filter":
            self.filterset_class,
            "rooms":
            rooms,
            "total_rooms":
            self.object_list.count(),
            "average_capacity": (self.object_list.aggregate(
                avg_capacity=Avg("capacity"))["avg_capacity"] or 0),
            "total_beds": (self.object_list.aggregate(
                total_beds=Count("capacity"))["total_beds"] or 0),
            "total_free_beds": (self.object_list.aggregate(
                total_free_beds=Sum("free_beds"))["total_free_beds"] or 0)
        }
        return ctx


class RoomDetailView(DetailView):
    model = Room
    context_object_name = "context"
    template_name = "content/room/detail/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super(RoomDetailView, self).get_context_data(**kwargs)
        room = ctx.pop("context")
        num_of_patients = len(Patient.objects.filter(room=room))
        num_of_nurses = len(Nurse.objects.filter(room_in_charge=room))
        ctx["context"] = {
            "room": room,
            "num_patients": num_of_patients,
            "free_beds": room.capacity - num_of_patients,
            "num_nurses": num_of_nurses,
            "nurses": Nurse.objects.filter(room_in_charge=room),
            "patients": Patient.objects.filter(room=room)
        }
        return ctx


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy("entities:list_room")
