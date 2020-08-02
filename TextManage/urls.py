# from django.conf.urls import url
from django.urls import path
from . import views

app_name ='TextManage'

urlpatterns = [
    path('TextManage', views.TextManageView),
    path('textlist',views.textlist,name='textlist'),
    # path('upload',views.Upload),
    path('upload',views.Upload.as_view(),name='upload')
    # path('submit',views.textadd,name='submit')
]