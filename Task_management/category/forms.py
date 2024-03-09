from django import forms 
from category.models import CategoryModel

class CatagoryForm(forms.ModelForm):
    class Meta:
        model =CategoryModel
        fields ='__all__'

    