from django import forms
from .models import Review

class orderForm(forms.ModelForm):

    heading = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Review
        fields = ['heading', 'review']