from django.shortcuts import render
import datetime

def home(request):
    d = {

        'author' : "korim",
        'join' :datetime.datetime.now(),
        'list': ['python','c','c++'],


    }
    return render(request,"home.html",d)