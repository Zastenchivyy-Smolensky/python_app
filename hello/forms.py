from django import forms
from django.forms import fields, widgets
from.models import Friend
from.models import Message
class CheckForm(forms.Form):
    
    str=forms.CharField(label="String",\
        widget=forms.TextInput(attrs={"class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        str=cleaned_data["str"]
        if(str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')
class FindForm(forms.Form):
    find = forms.CharField(label="Find",required=False,\
        widget=forms.TextInput(attrs={"class":"form-control"}))
class FriendForm(forms.ModelForm):
    class Meta:
        model=Friend
        fields=["name","mail","gender","age","birthday"]
        params={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "mail":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "birthday":forms.DateInput(attrs={"class":"form-control"}),
        }
class HelloForm(forms.Form):
    name=forms.CharField(label="Name",\
        widget=forms.TextInput(attrs={"class":"form-control"}))
    mail=forms.EmailField(label="Email",\
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    gender=forms.BooleanField(label="Gender",required=False,\
        widget=forms.CheckboxInput(attrs={"class":"form-control"}))
    age=forms.IntegerField(label="Age",\
        widget=forms.NumberInput(attrs={"class":"form-control"}))
    birthday=forms.DateField(label="Birth",\
        widget=forms.DateInput(attrs={"class":"form-control"}))
class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=["title","content","friend"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control form-control-sm"}),
            "content":forms.Textarea(attrs={"class":"form-control form-control-sm","rows":2}),
            "friend":forms.Select(attrs={"class":"form-control form-control-sm"}),
        }