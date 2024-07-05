from django import forms
from datetime import date

class ItemForm(forms.Form):
    name = forms.CharField(max_length=50)
    description =forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField(min_value=0)
    date_add = forms.DateField(initial=date.today, 
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    img = forms.ImageField()