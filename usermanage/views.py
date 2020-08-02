from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from usermanage.models import TUser

# Create your views here.
def loginView(request):
    return render(request, 'usermanage/Login.html')

def userAdd(request):
    return render(request, 'usermanage/AddUser.html')

def userManage(request):
    return render(request, 'usermanage/UserManagePage.html')

def userEdit(request):
    return render(request, 'usermanage/EditUser.html')

def resetPass(request):
    return render(request, 'usermanage/Reset.html')

def mainPage(request):
    return render(request, 'usermanage/Main_1.html')

def indexPage(request):
    return render(request, 'usermanage/Index.html')

def userInfo(request, userid):

    print('userid: ', userid)
    return render(request, 'usermanage/Login.html')

def loginInfo(request, username, userpwd):
    print('username: ', username)
    print('userpwd: ', userpwd)
    return render(request, 'usermanage/Login.html')

def loginAction(request):
    if request.method=='POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('password')
        ret = TUser.objects.filter(username=username,userpwd=userpwd)
        if 0 == len(ret):
            return HttpResponse('User does not exist!')
        else:
            global userid
            userid = ret[0].userid
            return render(request,'usermanage/Main_1.html',{'userid': userid})


def addUser(request):
    if request.method=='POST':
        new_user = TUser()
        new_user.username = request.POST.get('addusername')
        new_user.userpwd = request.POST.get('addpassword')
        new_user.save()
