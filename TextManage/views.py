from django.shortcuts import render, HttpResponse, redirect
from TextManage.models import TextMange
from django.views import View
import datetime
from TextAnalysisSystem3.settings import MEDIA_ROOT
import os,sys


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

        suffix = file.name.split(".")[1]
        print("suffix: {}".format(suffix))

        # if 'pdf' == suffix or 'docx' == suffix or 'doc' == suffix:
        #     # with open(file.name, 'wb') as f:
        #     with open(os.path.join(MEDIA_ROOT,file.name),'wb') as f:
        #         for i in file:
        #             f.write(i)
        #
        #     ret = TextMange.objects.create(pname=file.name,ptype=suffix,userid=userid,updatetime=datetime.datetime.now())
        #     return HttpResponse('OK')
        # else:
        #     return HttpResponse('NO')


        if 'pdf' == suffix or 'docx' == suffix or 'doc' == suffix:
            # with open(file.name, 'wb') as f:
            with open(os.path.join(MEDIA_ROOT,file.name),'wb') as f:
                for i in file:
                    try:
                        f.write(i)
                    except:
                        continue


            ret = TextMange.objects.create(pname=file.name,ptype=suffix,userid=userid,updatetime=datetime.datetime.now())
            return HttpResponse('OK')
        else:
            return HttpResponse('NO')




