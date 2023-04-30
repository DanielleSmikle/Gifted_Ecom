from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm, SetPasswordForm)
from .models import UserBase

class UserLoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    passwords = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))



class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label= 'Enter Username', min_length=4, max_length=50, help_text='Required')
    email_address = forms.EmailField(max_length=100, help_text ='Required', error_messages={'required': 'Sorry, you will need an email address'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label ='Repeat password', widget=forms.PasswordInput)

    class Meta: 
        model = UserBase
        fields = ('user_name', 'email_address',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('Username already exists')
        return user_name   #makeing sure usr makes unique user name 

    def clean_password2(self):
        cd= self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']   #making sure user password is correct 
    
    def clean_email_address(self):
        email_address = self.cleaned_data['email_address']
        if UserBase.objects.filter(email_address=email_address).exists():
            raise forms.ValidationError(
                'Please use another email address, that is already taken')
        return email_address
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email_address'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email_address', 'id': 'id_email_address'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})

     
        

    