from django import forms
from django.forms import ModelForm
from .models import Task




class Addtodo(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'name']

        

