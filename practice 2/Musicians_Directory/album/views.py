from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def album(request):
    if request.method =='POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =forms.AlbumForm()           
    return render(request,'album.html',{'form':form})
