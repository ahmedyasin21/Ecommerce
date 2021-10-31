from django.contrib.auth.models import User
from django import forms

from django.core.exceptions import ValidationError
from django.core import validators
from .models import ShopRequest
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from datetime import datetime
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib import messages




class ShopRequestForm(forms.ModelForm):
    
    class Meta:
        model = ShopRequest
        fields = ("first_name","last_name","age","gender","nationality","country","city","state","zip_code","user_address","shop_title","shop_category","shop_address")
        Gender = (
            ('male','Male'),
            ('female','Female'),
            )
            
        Cards = (
            ('silver','Silver'),
            ('gold','Gold'),
            ('diamond','Diamond'),
            )

        Wallets = (
            ('bitcoin','Bitcoin'),
            ('etherum','Ethereum'),
            ('fitoken','FIToken'),
            )

            
        widgets ={
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(choices=Gender,attrs={'class': 'form-control'}),
            'nationality' : forms.TextInput(attrs={'class':'form-control'}),
            'country': CountrySelectWidget(),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control'}),
            "user_address":forms.TextInput(attrs={'class':'form-control'}),
            "shop_address":forms.TextInput(attrs={'class':'form-control'}),
        }
  
   

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ShopRequestForm, self).__init__(*args, **kwargs)
        # self.fields['wallet_address'].disabled = True
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #     self.fields['wallet_address'].disabled = True

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get('age')
        print(age)
        if age < 18:
            # raise forms.ValidationError("You're age should be 18 plus")
            age = "You're age should be 18 plus"
            self.add_error('age',age)
            raise forms.ValidationError("You're age should be 18 plus")
