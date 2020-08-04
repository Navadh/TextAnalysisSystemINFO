from django.shortcuts import render, HttpResponse
from usermanage.models import TUser, MainControl
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url="/usermanage/index")

def indexall(request):
    return render(request, 'usermanage/Index_1.html')


def loginviewadmin(request):
    return render(request, 'usermanage/Login_A.html')


def loginviewuser(request):
    return render(request, 'usermanage/Login_U.html')


def useradd(request):
    return render(request, 'usermanage/AddUser.html')


def usermanage(request):
    all_users = TUser.objects.all().order_by('usercreatetime')
    return render(request, 'usermanage/UserManagePage.html', {'all_users': all_users})


def useredit(request):
    return render(request, 'usermanage/EditUser.html')


def userdelete(request):
    return render(request, 'usermanage/DeleteUser.html')

def resetpass(request):
    return render(request, 'usermanage/Reset.html')


def mainadmin(request):
    return render(request, 'usermanage/Main_A.html')


def mainuser(request):
    return render(request, 'usermanage/Main_U.html')


def sideadmin(request):
    return render(request, 'usermanage/Sideframe_A.html')


def sideuser(request):
    # user = request.session['nonadminuser']
    return render(request, 'usermanage/Sideframe_U.html')



def userinfoadmin(request, tadmin_id):
    print('tadmin_id: ', tadmin_id)
    return render(request, 'usermanage/Login_A.html')


def userinfouser(request, userid):
    print('userid: ', userid)
    return render(request, 'usermanage/Login_U.html')


def logininfoadmin(request, tadmin_name, tadmin_pwd):
    print('tadmin_name: ', tadmin_name)
    print('tadmin_pwd: ', tadmin_pwd)
    return render(request, 'usermanage/Login_A.html')


def logininfouser(request, username, userpwd):
    print('username: ', username)
    print('userpwd: ', userpwd)
    return render(request, 'usermanage/Login_U.html')


def loginactionadmin(request):
    if request.method == 'POST':
        controlname = request.POST.get('controlname')
        controlpwd = request.POST.get('controlpwd')
        ret = MainControl.objects.filter(controlname=controlname, controlpwd=controlpwd)
        # user_name = ret[0].username
        # request.session['nonadminuser'] = user_name
        if 0 == len(ret):
            return HttpResponse('Either the Admin name or password is not matching or the Admin user does not exist!')
        else:
            # userid = ret[0].userid
            return render(request, 'usermanage/Main_A.html')



def loginactionuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('password')
        # request.session['nonadminuser'] = username
        ret = TUser.objects.filter(username=username, userpwd=userpwd)
        user_name = ret[0].username
        # request.session['nonadminuser'] = user_name
        if 0 == len(ret):
            return HttpResponse('Either the username or password is not matching or the user does not exist!')
        else:
            # userid = ret[0].userid
            return render(request, 'usermanage/Main_U.html')
            # , {'userid': userid})

def adduser(request):
    if request.method == 'POST':
        new_user = TUser()
        new_user.username = request.POST.get('addusername')
        new_user.userpwd = request.POST.get('addpassword')
        new_user.save()
        return HttpResponse('New User created!')


def deleteuser(request):
    if request.method == 'POST':
        delete_user = TUser()
        delete_user.username = request.POST.get('deleteuser')
        delete_user.userid = request.POST.get('deleteuserid')
        delete_user.delete()
        return HttpResponse('User deleted!')


