from django.shortcuts import render,redirect
from .import forms 
from .import models 

# Create your views here.
def add_task(request):
    if request.method =='POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('category')
    else:
        form =forms.TaskForm()
    return render(request,'task.html',{'form':form})

def edittask(request,id):
    task =models.TaskModel.objects.get(pk=id)
    form =forms.EdiTaskForm(instance=task)
    if request.method =='POST':
        form=forms.EdiTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'edittask.html',{'form':form})


def delete(request,id):
    task =models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')


