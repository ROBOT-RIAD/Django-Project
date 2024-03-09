from django.urls import path
from .import views

urlpatterns = [
    path("add/",views.musician,name='misician'),
    path('edit/<int:id>',views.editmusician,name='editmusician'),
    path('delete/<int:id>',views.delete_m,name='deletes'),

]
