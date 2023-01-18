from django import forms
from .models import User

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    # password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'}))

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'email', 'phone_number', 'password', 'username']

    def clean(self):
        cleaned_data = super(userForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")


