from django import forms
from .models import Flightinfo


# creating a form

class Flightinfo_form(forms.ModelForm):
    class Meta:
        model = Flightinfo
        fields = "__all__"