"""
Here is the file that contains all the entity models.
"""
from django.db.models import (Model, CharField, PositiveIntegerField,
                              DecimalField, ForeignKey, SET_NULL, RESTRICT)
from django.core.validators import MaxValueValidator, MinValueValidator

# TODO: Add dockstrings


# ========= Base Models =========
class Human(Model):
    """Is the base for all people. Does the validations too."""
    name: CharField = CharField(max_length=40, null=False, blank=False)
    age: PositiveIntegerField = PositiveIntegerField(
        null=False, validators=[MinValueValidator(0),
                                MaxValueValidator(110)])

    class Meta:
        abstract = True


class Employee(Human):
    """
    Is the base for workers, like class Human it has validators that ensure
    the proper results for the workers.
    """
    age = PositiveIntegerField(
        null=False, validators=[MinValueValidator(21),
                                MaxValueValidator(67)])
    experience: PositiveIntegerField = PositiveIntegerField(null=False)
    salary: DecimalField = DecimalField(null=False,
                                        decimal_places=2,
                                        max_digits=10)

    class Meta:
        abstract = True


# ========= Entity Models =========
class Room(Model):
    """The model for the room"""
    number: PositiveIntegerField = PositiveIntegerField(
        null=False, unique=True, validators=[MinValueValidator(0)])
    capacity: PositiveIntegerField = PositiveIntegerField(
        null=False, validators=[MinValueValidator(1),
                                MaxValueValidator(4)])

    class Meta:
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"Room: {self.number}"


# TODO: validate the experience based on it's age.
class Doctor(Employee):
    """The model for the doctor entity."""

    class Meta:
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"Doctor: {self.name}"


class Nurse(Employee):
    """The model for the nurse entity."""
    room_in_charge: ForeignKey = ForeignKey(Room,
                                            null=True,
                                            on_delete=SET_NULL)

    class Meta:
        verbose_name_plural = "Nurses"

    def __str__(self):
        return f"Nurse: {self.name}"


class Patient(Human):
    """The model for the patient entity."""
    disease: CharField = CharField(max_length=60, null=False, blank=False)
    # The patient won't be deleted incase the room is deleted.
    room: ForeignKey = ForeignKey(Room, null=False, on_delete=RESTRICT)
    # The patient won't be deleted incase the doctor is deleted.
    doctor: ForeignKey = ForeignKey(Doctor, null=False, on_delete=RESTRICT)

    class Meta:
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"Patient: {self.name}"
