from django import forms
from .models import Record

class addRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First_name', "class":'form-control form-floating'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last_name', "class":'form-control'}))
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'email', "class":'form-control'}))
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'phone', "class":'form-control'}))
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'address', "class":'form-control'}))
    city=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'city', "class":'form-control'}))
    state=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'state', "class":'form-control'}))
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'zipcode', "class":'form-control'}))

    class Meta:
        model = Record
        exclude = ('user',)