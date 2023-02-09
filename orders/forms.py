from django import forms
from .models import Order

class orderForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class':'form-control'}))

    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label='city', widget=forms.TextInput(attrs={'class':'form-control'}))
    pin_code = forms.CharField(label='Pin Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    services = forms.CharField(label='services', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Select Service From Top Line'}))

    class Meta:
        model = Order
        fields = ['first_name' , 'last_name', 'email', 'phone', 'address', 'state', 'city', 'pin_code', 'date']
        widgets = {
        'date': forms.DateInput(
        format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
        }