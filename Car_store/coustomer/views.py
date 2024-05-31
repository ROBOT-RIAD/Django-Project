from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from Car.models  import Cars
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

# signup form
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form =forms.SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully.')
                form.save()
                return redirect('login')
        else:
            form =forms.SignupForm()
        return render(request,'form.html',{'form':form,'type':'Signup'})
    
class user_login(LoginView):
    template_name = 'form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,'Login Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Username and password not Correct')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['type'] ='Login'
        return context
    



class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

@login_required       
def user_car(request):
    car = Cars.objects.filter(coustomer=request.user)
    return render(request, 'profile.html', {'cars': car}) 


