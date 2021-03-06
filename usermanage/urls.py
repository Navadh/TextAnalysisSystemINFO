# from django.conf.urls import url
from django.urls import path
from . import views


app_name ='usermanage'

urlpatterns = [
    path('loginadmin', views.loginviewadmin),
    path('loginuser', views.loginviewuser),
    path('<int:userid>',views.userinfoadmin),
    path('<int:userid>',views.userinfouser),
    path('index', views.indexall),
    # path('<slug:username>/<slug:userpwd>',views.logininfoadmin),
    # path('<slug:username>/<slug:userpwd>',views.logininfouser),
    path('loginactionadmin', views.loginactionadmin),
    path('loginactionuser', views.loginactionuser),
    path('adduser', views.adduser),
    # path('testing', views.testing),
    path('useradd', views.useradd),
    path('edituser', views.useredit),
    path('edit/<int:userid>/<slug:username>/<slug:userpwd>', views.user_edit.as_view()),
    path('useredit', views.editeuser),
    path('userdelete', views.userdelete),
    path('delete/<int:userid>', views.user_del.as_view()),
    path('deleteuser', views.deleteuser),
    path('usermanage', views.usermanage),
    path('reset', views.resetpass),
    path('mainadmin', views.mainadmin),
    path('mainuser', views.mainuser),
    path('sideadmin', views.sideadmin),
    path('sideuser', views.sideuser),
    # path('sideuserload/<slug:username>', views.sideuser),

]