from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path("form/",views.form_api,name='form_api'),
    path('django/',views.djangoform,name='django'),
    path('show/',views.djangoshow,name='show'),
]
