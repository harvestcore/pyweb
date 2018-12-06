from django import forms

from .models import Plato


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['chef', 'tipoCocina', 'alergenos', 'precio', 'nombre', 'descripccion', 'ingredientes']


class SearchForm(forms.Form):
    name = forms.CharField(max_length=30, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'id': 'ajaxSearchName'}))
    _id = forms.CharField(max_length=30, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'ID'}))

class EditForm(forms.Form):
    name = forms.CharField(max_length=30, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    coordinates = forms.CharField(max_length=30, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Coordenadas'}))
    locationtype = forms.CharField(max_length=15, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Tipo'}))

class AddForm(forms.Form):
    name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    coordinates = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Coordenadas'}))
    locationtype = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Tipo'}))