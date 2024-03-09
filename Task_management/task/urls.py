from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.add_task,name='task'),  
    path('edit/<int:id>',views.edittask,name='edittask'),  
    path('delete/<int:id>',views.delete,name='delete'),  
]
