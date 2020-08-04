import os

from django.shortcuts import render, HttpResponse, redirect
from TextManage.models import TextMange
from django.views import View
import datetime
from TextAnalysisSystem3.settings import MEDIA_ROOT

# Create your views here.
def TextManageView(request,userid):
    all_textmanages = TextMange.objects.all()
    return render(request,'TextManage.html',{'all_textmanages': all_textmanages,'userid':userid})

def textlist(request):
    all_textmanages =TextMange.objects.all()
    return render(request,'text_list.html',{'all_textmanages': all_textmanages})


class Upload(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request,userid):

        file = request.FILES.get('f1')
        # 获取文件名后缀
        suffix = file.name.split(".")[1]
        print("suffix: {}".format(suffix))
        # 判断后缀
        if 'pdf' == suffix or 'docx' == suffix or 'doc' == suffix or 'txt' == suffix:
            with open(os.path.join(MEDIA_ROOT,file.name), 'wb') as f:
                for i in file:
                    f.write(i)

            ret = TextMange.objects.create(pname=file.name,ptype=suffix,userid=userid,updatetime=datetime.datetime.now())
            return HttpResponse('OK')
        else:
            return HttpResponse('NO')


        # ttextmanageid = request.GET.get('ttextmanageid')
        # TextMange.objects.get(ttextmanageid=ttextmanageid).delete()
        # return render(request,'upload.html',{'ttextmanageid':ttextmanageid})


