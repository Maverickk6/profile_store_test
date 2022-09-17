from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signUp, name='signup'),
    path('users', views.usersList, name='users'),
]