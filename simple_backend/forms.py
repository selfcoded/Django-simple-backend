from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Record


class SignUpForm(UserCreationForm):
    email: forms.EmailField(label='', widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email Address'}))
    first_name: forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}))
    last_name: forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label= ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Required</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label= ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><li> Required</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat password'
        self.fields['password2'].label= ''
        self.fields['password2'].help_text = '<ul class="form-text text-muted"><li> Required</li></ul>'

class CustomForm(ModelForm):
    first_name = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name', 'helptext':None}))
    last_name = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email'}))
    phone = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Phone'}))
    address = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Address'}))
    city = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'City'}))
    state = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'State'}))
    zipcode = forms.CharField(required=True, label='', max_length=100, widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'zipcode'}))

    class Meta:
        model = Record
        # fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        fields = ['first_name','last_name','email','phone','address','city','state','zipcode']
