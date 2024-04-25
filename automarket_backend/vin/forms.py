from django import forms

class VinForm(forms.Form):
    vin = forms.CharField(label='VIN', max_length=17)
