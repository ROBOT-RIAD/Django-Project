from django.shortcuts import render
from category.models import CategoryModel

def home(request):
    data =CategoryModel.objects.all()
    return render(request,'home.html',{'data':data})