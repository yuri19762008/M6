
# book/forms.py
from django import forms

class BookForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=True)
    autor = forms.CharField(max_length=150, required=True)
    valoracion = forms.IntegerField(min_value=0, max_value=10000, required=True)