from django.contrib import admin
from django.urls import include, path

from .views import login_view, register_view, home_view, logout_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('', home_view, name="home"),
    path('logout/', logout_view, name='logout'),
]
