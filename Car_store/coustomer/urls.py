from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/",views.user_login.as_view(),name="login"),
    # path("profile/",views.profile,name="profile"),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('usercars/', views.user_car, name='user_cars'),
]
