"""
Here is the file that contains all the entity models.
"""
from django.db.models import (Model, CharField, PositiveIntegerField, DecimalField, ForeignKey, SET_NULL, RESTRICT)
from django.core.validators import MaxValueValidator, MinValueValidator 
# TODO: Add dockstrings



# ========= Base Models =========
class Human(Model):
    name = CharField(max_length=40, null=False, blank=False)
    age = PositiveIntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(110)])

    class Meta:
        abstract=True


class Employee(Human):
    age = PositiveIntegerField(null=False, validators=[MinValueValidator(21), MaxValueValidator(67)])
    experience = PositiveIntegerField(null=False)
    salary = DecimalField(null=False, decimal_places=2,max_digits=10)
    
    class Meta:
        abstract=True


# ========= Entity Models =========
class Room(Model):
    number = PositiveIntegerField(null=False,unique=True, validators=[MinValueValidator(0)])
    capacity = PositiveIntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(4)])

    class Meta:
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"Room: {self.number}"


# TODO: validate the experience based on it's age.
class Doctor(Employee):

    class Meta:
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"Doctor: {self.name}"


class Nurse(Employee):
    room_in_charge=ForeignKey(Room, null=True, on_delete=SET_NULL)

    class Meta:
        verbose_name_plural = "Nurses"

    def __str__(self):
        return f"Nurse: {self.name}"

class Patient(Human):
    disease= CharField(max_length= 60, null=False, blank= False)
    room=ForeignKey(Room, null=False, on_delete=RESTRICT) 
    doctor=ForeignKey(Doctor, null=False, on_delete=RESTRICT)

    class Meta:
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"Patient: {self.name}"