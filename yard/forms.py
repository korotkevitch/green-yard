from django import forms
from django.forms import ModelForm
from .models import Feedback


class UserForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)