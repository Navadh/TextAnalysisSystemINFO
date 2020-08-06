# from django.conf.urls import url
from django.urls import path
from . import views
#from .views import testfreqdata

app_name ='TextAnalysis'

urlpatterns = [
    path('mainpage', views.PAnalysisview),
    path('abc', views.testfreqdata),

    path('textanlysis',views.textanalysis.as_view()),


    # path('<int:userid>',views.userInfo),
    # path('<slug:username>/<slug:userpwd>',views.loginInfo),
    # path('loginaction', views.loginAction),
    # path('adduser', views.addUser),
    # path('useradd', views.userAdd),
    # path('edituser', views.userEdit),
    # path('usermanage', views.userManage),
    # path('reset', views.resetPass),
    # path('index', views.indexPage),
    # path('main', views.mainPage),
]