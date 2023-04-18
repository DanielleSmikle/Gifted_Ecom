from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm, SetPasswordForm)
from .models import UserBase


class RegistrationForm(forms.ModelForm):
        user_name = forms.CharField(label= 'Enter Username', min_length=4, max_length=50, help_text='Required')
        email = forms.EmailField(max_length=100, help_text ='Required', error_messages={'required': 'Sorry, you will need an emaail'})
        password = forms.CharField(label='Password', widget=forms.PasswordInput)
        password2 = forms.CharField(label ='Repeat password', widget=forms.PasswordInput)

        class Meta: 
            model = UserBase
            fields = ('user_name', 'email',)

    def clean_username(self):
      user_name = self.cleaned_data['user_name'].lower()
      r = User.Base.objects.filter(user)

    