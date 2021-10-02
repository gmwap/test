from hello.models import Friend
from django import forms


class HelloForm(forms.Form):
    #id = forms.IntegerField(label='ID')
    name=forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail=forms.CharField(label='Mail', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    gneder= forms.BooleanField(label='Gender', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age=forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday=forms.DateField(label='Birth', \
        widget=forms.DateInput(attrs={'class':'form-control'}))


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']