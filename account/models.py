from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email_address, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email_address, user_name, password, **other_fields)
    
    def create_user(self, email_address, user_name, password, **other_fields):
        if not email_address:
            raise ValueError(_('You must provide an email_address address'))
        
        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
class UserBase(AbstractBaseUser, PermissionsMixin):
    #usr/delievery info
    email_address = models.EmailField(max_length=150, default='emails@email.com', unique=True)
    user_name = models.CharField(max_length=150, unique= True)
    first_name= models.CharField(max_length=150, blank= True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    country = CountryField()
    phone_number = models.CharField(max_length=15, blank=True)
    address_line_1= models.CharField(max_length=150, blank=True)
    address_line_2= models.CharField(max_length=150, blank=True)
    town_city= models.CharField(max_length=150, blank=True)
    #user status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    objects = CustomAccountManager()

    USERNAME_FIELD ='email_address'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural ='Accounts'
    def __str__(self):
        return self.user_name
    

    


 