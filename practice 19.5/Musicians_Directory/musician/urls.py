from django.urls import path
from .import views

urlpatterns = [
    path("add/",views.musician.as_view(),name='misician'),
    path('edit/<int:pk>',views.editmusician.as_view(),name='editmusician'),
    path('delete/<int:pk>',views.delete_m.as_view(),name='deletes'),
]
