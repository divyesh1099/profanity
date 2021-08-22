from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import demoImage

class demoImageForm(forms.ModelForm):
    class Meta:
        model = demoImage
        fields = ('dimg',)
        widgets = {

        }