from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import Department, Semester


class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    sem = forms.CharField(help_text='Sem',  widget=forms.Select(choices=Semester))
    dept = forms.CharField(help_text='Dept',widget=forms.Select(choices= Department))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'email', 'sem', 'dept', 'password1', 'password2', )