"""Docstring."""
from django.contrib import admin
from .models import Nurse, Person, Bed, Bed_History

admin.site.register(Nurse)
admin.site.register(Bed)
admin.site.register(Bed_History)
admin.site.register(Person)
