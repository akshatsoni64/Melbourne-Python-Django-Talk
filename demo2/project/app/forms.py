from django import forms

class AdditionForm(forms.Form):
    a = forms.IntegerField(max_value=1000)
    b = forms.IntegerField(max_value=1000)