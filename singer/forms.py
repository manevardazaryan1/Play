from django import forms

# singer app forms.py

class SingerSearchForm(forms.Form):
    """Singer search form class"""

    name = forms.CharField(required=False)
    search = forms.CharField(initial='True', widget=forms.HiddenInput())
