from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def musician(request):
    if request.method =='POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form =forms.MusicianForm()           
    return render(request,'musician.html',{'form':form})

def editmusician(request,id):
    musican = models.MusicianModel.objects.get(pk=id)
    form=forms.MusicianForm(instance=musican)
    if request.method =="POST":
        form=forms.MusicianForm(request.POST,instance=musican)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'musician.html',{'form':form})


def delete_m(request,id):
    musican = models.MusicianModel.objects.get(pk=id)
    musican.delete()
    return redirect('home')

