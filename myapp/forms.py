from dataclasses import field
from pyexpat import model
from django import forms
from .models import Image
from django.forms import ModelForm


class ImageAdmin(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'slug', 'tags', 'image']