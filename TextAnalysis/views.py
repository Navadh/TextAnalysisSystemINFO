from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
# import nltk
# import sys
# import codecs
# from datascience import *
# import numpy as np
#from TextAnalysis.processingscripts.freqplot2 import freqtable
from TextAnalysis.processingscripts.freqplot2speech import freqtable
from TextAnalysisSystem3.settings import MEDIA_ROOT
from TextAnalysisSystem3.settings import STATICFILES_DIRS
import os
from django.views import View
from TextAnalysis.models import WFreq
import TextManage.views

#from usermanage.models import TUser

# Create your views here.
def PAnalysisview(request):
    return render(request, 'PassageAnalysis.html')

def testfreqdata(request):
    # filename = os.path.join(MEDIA_ROOT,"cnnkofile.txt")
    # def post(self, request, pname):
    #     # TUser.objects.filter(userid=userid).delete()
    #     ret = TextMange.objects.filter(pname=pname)
    #     pname = ret[0].pname
    if request.session.has_key('pname'):
        pname = request.session['pname']
    # ret = TextMange.objects.filter(pname=pname)
    # pname = ret[0].pname

    # print(pname)
    filename = os.path.join(MEDIA_ROOT, {'pname': pname})
    # print(filename)

    #result = freqtable("/Users/rajeshpahari/PycharmProjects/FinalProject/Media/textfile1.txt")
    result = freqtable(filename)
    # print("here comes the variable")
    # print(request.session['nonadminuser'])
  # result should be a string
    print("You will see this word in the console:", result)
    return render(request, 'TextAnalysis2.html', {'pname': pname})
    #return HttpResponse(result)


class textanalysis(View):
    def get(self,request):
        return render(request,'PassageAnalysis.html')
    def post(self,request):
        all_textanalysis= WFreq.objects.all()
        return render(request,'PassageAnalysis.html',{'all_textanalysis':all_textanalysis})


# def loginView(request):
#     return render(request, 'usermanage/Login.html')
#
# def userAdd(request):
#     return render(request, 'usermanage/AddUser.html')
#
# def userManage(request):
#     return render(request, 'usermanage/UserManagePage.html')
#
# def userEdit(request):
#     return render(request, 'usermanage/EditUser.html')
#
# def resetPass(request):
#     return render(request, 'usermanage/Reset.html')
#
# def mainPage(request):
#     return render(request, 'usermanage/Main_1.html')
#
# def indexPage(request):
#     return render(request, 'usermanage/Index.html')
#
# def userInfo(request, userid):
#
#     print('userid: ', userid)
#     return render(request, 'usermanage/Login.html')
#
# def loginInfo(request, username, userpwd):
#     print('username: ', username)
#     print('userpwd: ', userpwd)
#     return render(request, 'usermanage/Login.html')
#
# def loginAction(request):
#     if request.method=='POST':
#         username = request.POST.get('username')
#         userpwd = request.POST.get('password')
#         ret = TUser.objects.filter(username=username,userpwd=userpwd)
#         if 0 == len(ret):
#             return HttpResponse('User does not exist!')
#         else:
#             global userid
#             userid = ret[0].userid
#             return render(request,'usermanage/Main_1.html',{'userid': userid})
#
#
# def addUser(request):
#     if request.method=='POST':
#         new_user = TUser()
#         new_user.username = request.POST.get('addusername')
#         new_user.userpwd = request.POST.get('addpassword')
#         new_user.save()
class user_analysis(View):
    def get(self, request):
        return render(request, 'TextAnalysis2.html')

    def post(self, request, pname):
        # TUser.objects.filter(userid=userid).delete()
        ret = TTextManage.objects.filter(pname=pname)
        pname = ret[0].pname
        # username = ret[0].username
        # userpwd = ret[0].userpwd
        # all_users = TUser.objects.all()
        return render(request, 'TextAnalysis2.html', {'pname': pname})