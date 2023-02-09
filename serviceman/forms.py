from django import forms
from accounts.models import User
from .models import Serviceman

class ServicemanForm(forms.ModelForm):
    class Meta:
        model = Serviceman
        fields = ['serviceman_id']

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class':'form-control'}))

    

    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'email', 'phone_number']


