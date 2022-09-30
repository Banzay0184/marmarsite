from django import forms
from .models import *


class ConatactForms(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ваше имя'
    }))
    numbers = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Номер телефона'
    }))

    class Meta:
        model = ContactModel
        fields = ('name', 'numbers')


class ReviewsForms(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ваше имя'
    }))
    massage = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Номер телефона'
    }))

    class Meta:
        model = Reviews
        fields = ('name', 'massage')
