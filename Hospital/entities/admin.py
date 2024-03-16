from django.contrib import admin
from entities.models import (
    Room,
    Doctor,
    Patient,
    Nurse
)

admin.site.register(Room)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)
