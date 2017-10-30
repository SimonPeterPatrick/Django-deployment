# -*- coding: utf-8 -*-
from django.conf.urls import url
from app_base import views

app_name = 'app_base'

urlpatterns = [
        url(r'^register/$',views.register, name='register'),
        url(r'^user_login/$',views.user_login,name='user_login')
        ]