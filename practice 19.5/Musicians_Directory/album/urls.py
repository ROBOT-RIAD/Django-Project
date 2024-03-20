from django.urls import path
from .import views

urlpatterns = [
    path("add/",views.album.as_view(),name='album')
]
