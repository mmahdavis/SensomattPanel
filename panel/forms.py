"""Docstring."""

from django import forms
from models.models import Bed, Nurse, Bed_History, Person


class insertbed_form(forms.ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Bed
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Docstring."""
        super(insertbed_form, self).__init__(*args, **kwargs)
        """Docstring."""
        self.fields['nurse'].required = False
        self.fields['person'].required = False


class insertnurse_form(forms.ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Nurse
        fields = '__all__'


class insertbedhistory_form(forms.ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Bed_History
        fields = '__all__'


class insertpatient_form(forms.ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Person
        fields = '__all__'
