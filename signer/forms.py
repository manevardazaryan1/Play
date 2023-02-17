from django import forms

# signer app forms.py

class SignerSearchForm(forms.Form):
    """Signer search form class"""

    first_name= forms.CharField(required=False)
    last_name= forms.CharField(required=False)
    search = forms.CharField(initial='True', widget=forms.HiddenInput())
