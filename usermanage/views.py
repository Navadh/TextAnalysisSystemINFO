from django.shortcuts import render
from usermanage.models import TUser

# Create your views here.


def indexall(request):
    return render(request, 'usermanage/Index_1.html')


def loginviewadmin(request):
    return render(request, 'usermanage/Login_A.html')


def loginviewuser(request):
    return render(request, 'usermanage/Login_U.html')


def useradd(request):
    return render(request, 'usermanage/AddUser.html')


def usermanage(request):
    return render(request, 'usermanage/UserManagePage.html')


def useredit(request):
    return render(request, 'usermanage/EditUser.html')


def resetpass(request):
    return render(request, 'usermanage/Reset.html')


def mainadmin(request):
    return render(request, 'usermanage/Main_A.html')


def mainuser(request):
    return render(request, 'usermanage/Main_U.html')


def sideadmin(request):
    return render(request, 'usermanage/Sideframe_A.html')


def sideuser(request):
    return render(request, 'usermanage/Sideframe_U.html')


def userinfoadmin(request, userid):
    print('userid: ', userid)
    return render(request, 'usermanage/Login_A.html')


def userinfouser(request, userid):
    print('userid: ', userid)
    return render(request, 'usermanage/Login_U.html')


def logininfoadmin(request, username, userpwd):
    print('username: ', username)
    print('userpwd: ', userpwd)
    return render(request, 'usermanage/Login_A.html')


def logininfouser(request, username, userpwd):
    print('username: ', username)
    print('userpwd: ', userpwd)
    return render(request, 'usermanage/Login_U.html')


def loginactionadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        print(username)
        print(userpwd)
        return render(request, 'usermanage/Main_A.html')


def loginactionuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        print(username)
        print(userpwd)
        return render(request, 'usermanage/Main_U.html')


def adduser(request):
    if request.method == 'POST':
        new_user = TUser()
        new_user.username = request.POST.get('addusername')
        new_user.userpwd = request.POST.get('addpassword')
        new_user.save()
