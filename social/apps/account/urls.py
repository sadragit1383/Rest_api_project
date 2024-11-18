from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('register/',RegisterUserApiView.as_view(),name='register'),
    path('users/',ListUserGeneric.as_view(),name='list_user'),
    path('users/<int:pk>/',ListUserDetail.as_view(),name='detail'),
    path('active_code/',ActiveCodeGeneric.as_view(),name='active_code'),
    path('login/',LoginUserGeneric.as_view(),name='login'),
    path('remmber_password/',RememberPassword.as_view(),name='remmber_passoword'),
    path('change_password/',ChangePassword.as_view(),name='change_password')

]
