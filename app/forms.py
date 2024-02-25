from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UserRegistration(forms.ModelForm):
    firstName = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter first Name'})
    lastName = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter last Name'})
    email = forms.EmailField(max_length=200,required=True,error_messages={'required':'Please enter Email'})
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(),error_messages={'required':'Please enter Your Password'})
    username = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter Username'})
    class Meta:
        model = User
        fields = ['firstName','lastName','email','password','username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email already used'))
        return email
    
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password) < 8:
    #         raise forms.ValidationError(_("Password must be at least 8 characters long."))
    #     return password
    

class UserLogin(forms.Form):
    username = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter your USERNAME'})
    password = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter your PASSWORD'})

class ProfileUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        # widgets = {'first_name':{'disabled':True}}

class SearchUser(forms.Form):
    search = forms.CharField(max_length=200)

    def search_empty(self):     #it will not run automatically we need to explicitly call it
        empty = self.cleaned_data['search']
        if not empty:
            raise forms.ValidationError('please enter value')
        return empty
    