from django.shortcuts import render
from first_app.forms import PracticeForm,DjangoModel
from .import models

def home(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'comment': form.cleaned_data['comment'],
                'agree': form.cleaned_data['agree'],
                'birthday': form.cleaned_data['birthday'],
                'expect_year': form.cleaned_data['expact_yer'],
                'day': form.cleaned_data['day'],
                'value': form.cleaned_data['value'],
                'favorite_colore': form.cleaned_data['favorite_colore'],
                'favorite_color': form.cleaned_data['favorite_color'],
            }
            
          
            return render(request, 'home.html', {'form_data': form_data})
    else:
        form = PracticeForm()
    return render(request, 'forms.html', {'form': form, 'form_data': None})

def form_api(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            

            form.save()
            return render(request, 'forms.html')
    else:
        form = PracticeForm()
    return render(request, 'forms.html', {'form': form})

def djangoform(request):
    if request.method =='POST':
        form =DjangoModel(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DjangoModel()
    return render(request,'django.html',{'form':form})


def djangoshow(request):
    form=models.DjangoForm.objects.all()
    return render(request,'show_data.html',{'data':form})