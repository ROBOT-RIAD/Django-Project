from django import forms
import datetime
from first_app.models import DjangoForm




class PracticeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Enter your comment'}),required=False)
    agree =forms.BooleanField(help_text="Accept all policies")
    # datefield 
    birthday = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    # year choices
    year_choices=['1900','1999','2000'] 
    expact_yer=forms.DateField(label='choices year',widget=forms.SelectDateWidget(years=year_choices))
    day =forms.DateField(initial=datetime.date.today)
    value=forms.DecimalField()
    # choices field 
    colore=[('b','blue'),('g','Green'),('r','red')]
    favorite_colore=forms.ChoiceField(label='single colore',choices=colore,widget=forms.RadioSelect)

    colore=[('b','blue'),('g','Green'),('r','red')]
    favorite_color=forms.MultipleChoiceField(choices=colore,widget=forms.CheckboxSelectMultiple)


class DjangoModel(forms.ModelForm):
    class Meta:
        model =DjangoForm
        fields='__all__'
        widgets ={
            'father_name' : forms.TextInput()
        }








    

    
