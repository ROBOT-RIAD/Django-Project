from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .import models
from . import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.



@method_decorator(login_required,name ='dispatch')
class CarDetaile(DetailView):
    model =models.Cars
    pk_url_kwarg ='id'
    template_name ='detaile.html'

    def post(self,request,*args,**kwargs): 
        comment_form =forms.CommentForm(data =self.request.POST)
        post =self.get_object()
        if comment_form.is_valid():
            new_comment =comment_form.save(commit=False)
            new_comment.post =post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        post =self.object
        comments = post.comments.all()
        comment_form =forms.CommentForm()

        context['comments'] =comments
        context['comment_form'] =comment_form
        return context
    
@login_required
def buy_car(request, id):
    car = get_object_or_404(models.Cars, pk=id)
    car.coustomer= request.user 
    car.quantity -=1
    car.save() 
    return redirect("home")


    
    


