# from django.conf.urls import url
from django.urls import path
from . import views

app_name ='TextManage'

urlpatterns = [
    path('TextManage/<int:userid>', views.TextManageView),
    path('textlist',views.textlist),
    path('upload/<int:userid>',views.Upload.as_view()),
    # path ('ManageText', views.TextManage),
    path('delete/<int:ttextmanageid>',views.text_del.as_view()),
    path('textanlysis',views.textanalysis.as_view()),
    path('abc', views.testfreqdata),
]