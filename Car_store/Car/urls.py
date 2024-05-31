from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.CarDetaile.as_view(), name='details'),
    path('buyecar/<int:id>/', views.buy_car, name='buyecar'),
]
