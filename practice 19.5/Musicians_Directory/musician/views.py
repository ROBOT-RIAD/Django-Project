from django.shortcuts import render,redirect
from album.models import AlbumModel
from album.forms import AlbumForm
from .import models
from .import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
# def musician(request):
#     if request.method =='POST':
#         form=forms.MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('album')
#     else:
#         form =forms.MusicianForm()           
#     return render(request,'musician.html',{'form':form})


class musician(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name ='musician.html'
    success_url =reverse_lazy('album')
    def form_valid(self, form):
        return super().form_valid(form)





# def editmusician(request,id):
#     musican = models.MusicianModel.objects.get(pk=id)
#     form=forms.MusicianForm(instance=musican)
#     if request.method =="POST":
#         form=forms.MusicianForm(request.POST,instance=musican)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     return render(request,'musician.html',{'form':form})

class editmusician(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name ='musician.html'
    success_url =reverse_lazy('home')



# def delete_m(request,id):
#     musican = models..objects.get(pk=id)
#     musican.delete()
#     return redirect('home')


class delete_m(DeleteView):
    model =AlbumModel
    template_name ='delete.html'
    success_url =reverse_lazy('home')



