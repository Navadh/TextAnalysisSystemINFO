from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from usermanage.models import TUser



def loginAction(request):
    if request.method=='POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('password')
        ret = TUser.objects.filter(username=username,userpwd=userpwd)
        if 0 == len(ret):
            return HttpResponse('User does not exist!')
        else:
            userid = ret[0].userid
            return render(request,'usermanage/Main_1.html',{'userid': userid})