from django.shortcuts import render,redirect
from .import forms 

# Create your views here.

def add_category(request):
    if request.method =='POST':
        form =forms.CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
    else:
        form=forms.CatagoryForm()
    return render(request,'category.html',{'form':form})

