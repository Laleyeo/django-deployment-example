from django.urls import re_path
from basic_app import views
from django.urls import path, re_path, include
from basic_app import views
from basic_app import urls


#template URLs
app_name = 'basic_app'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    re_path(r'^$',views.index,name='index'),
]
