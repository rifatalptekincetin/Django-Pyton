from django import forms
from linkler.models import link
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class linkform(forms.ModelForm):
    class Meta:
        model = link
        fields = ('link','aciklama','ad','resim')

class profileform(forms.ModelForm):
    class Meta:
        model=User
        fields={
            'first_name',
            'last_name',
            'email'}
