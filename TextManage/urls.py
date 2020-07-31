# from django.conf.urls import url
from django.urls import path
from . import views

app_name ='TextManage'

urlpatterns = [
    path('TextManage', views.TextManageView),
]