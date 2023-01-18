from django import forms
from .models import Serviceman

class ServicemanForm(forms.ModelForm):
    class Meta:
        model = Serviceman
        fields = ['serviceman_id']