"""Docstring."""
from django.db import models


class Nurse(models.Model):
    """Docstring."""

    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    shift = models.CharField(max_length=2, choices=(('D', 'Day'), ('N', 'Night'), ('LN', 'Late Night')), null=False)

    def __str__(self):
        """Docstring."""
        return str(self.name)


class Bed(models.Model):
    """Docstring."""

    number = models.IntegerField(null=False, blank=False)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True)
    bedsore = models.ImageField(upload_to='bedsores', null=True, blank=True)

    def __str__(self):
        """Docstring."""
        return str(self.number)


class Person(models.Model):
    """Docstring."""

    name = models.CharField(max_length=50, null=False, blank=False)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    age = models.SmallIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=False)
    sickness = models.CharField(max_length=30, null=True, default="")
    bed = models.OneToOneField(Bed, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        """Docstring."""
        return str(self.name)


class Bed_History(models.Model):
    """Docstring."""

    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, default="")
    date = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    sickness = models.CharField(max_length=30, null=False, blank=False)
    nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Docstring."""
        return str(self.date) + " bed number: " + str(self.bed)
