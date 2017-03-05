from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Organization name')
    email = forms.EmailField(label='Organization email')
    trial_period = forms.CheckboxInput()
