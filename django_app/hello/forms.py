from django import forms

class HelloForm(forms.Form):
    name=forms.CharField(label='名前', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail=forms.CharField(label='メール', widget=forms.TextInput(attrs={'class':'form-control'}))
    age=forms.IntegerField(label='年齢', widget=forms.NumberInput(attrs={'class':'form-control'}))