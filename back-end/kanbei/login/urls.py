from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^in$', views.loginSystem, name='login'),
    url(r'^out$', views.logoutSystem, name='logout'),
    url(r'^register$', views.registerSystem, name='register'),
]
