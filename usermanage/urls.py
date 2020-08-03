# from django.conf.urls import url
from django.urls import path
from . import views

app_name ='usermanage'

urlpatterns = [
    path('login', views.loginView),
    path('<int:userid>',views.userInfo),
    path('index/<int:userid>', views.indexPage),
    path('<slug:username>/<slug:userpwd>',views.loginInfo),
    path('loginaction', views.loginAction),
    path('adduser', views.addUser),
    path('useradd', views.userAdd),
    path('edituser', views.userEdit),
    path('usermanage', views.userManage),
    path('reset', views.resetPass),
    path('main', views.mainPage),
]