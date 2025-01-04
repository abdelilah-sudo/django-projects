from django.urls import path,include
from .views import Sign_upView,home
from django.contrib.auth.views import LoginView,LogoutView



app_name = 'accounts'
urlpatterns = [
    path('',home,name='home'),
    path("sign-up/",Sign_upView,name = 'sign-up'),
    path("login/",LoginView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
