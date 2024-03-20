from django.urls import path
from .views import home,signup,user_login,profile,user_logout,passchange,forgetpass

urlpatterns = [
    path("",home,name='home'),
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/',user_logout,name='logout'),
    path('passchange/',passchange,name='passchange'),
    path('forgetpass/',forgetpass,name='forgetpass'),
]
