from django import forms
from django.db.models import Max, Min

from .models import Music

# music app forms.py

class MusicSearchForm(forms.Form):
    """Music search form class"""

    name = forms.CharField(required=False)
    genre = forms.CharField(required=False)
    search = forms.CharField(initial='True', widget=forms.HiddenInput())

