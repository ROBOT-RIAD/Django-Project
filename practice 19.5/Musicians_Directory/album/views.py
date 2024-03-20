from django.shortcuts import render,redirect
from .import forms
from .import models
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
# def album(request):
#     if request.method =='POST':
#         form=forms.AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form =forms.AlbumForm()           
#     return render(request,'album.html',{'form':form})


class album(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name ='album.html'
    success_url =reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)
    

