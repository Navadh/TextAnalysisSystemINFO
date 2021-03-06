from django.shortcuts import render, HttpResponse, redirect
from TextManage.models import TextMange
from django.views import View
import datetime
from TextAnalysisSystem3.settings import MEDIA_ROOT
import os
from TextAnalysis.models import WFreq
# import django
# os.environ.setdefault("DJANGO_SETTING_MODULE", "TextAnalysisSystem3.settings")
# django.setup()

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
        pname = file.name.split(".")[0]
        print("suffix: {}".format(suffix))
        if 'pdf' == suffix or 'docx' == suffix or 'doc' == suffix:
            # with open(file.name, 'wb') as f:
            with open(os.path.join(MEDIA_ROOT,file.name),'wb') as f:
                for i in file:
                    try:
                        f.write(i)
                    except:
                        continue

            ret = TextMange.objects.create(pname=pname,ptype=suffix,userid=userid,updatetime=datetime.datetime.now())
            return HttpResponse('OK')
        else:
            return HttpResponse('NO')



class text_del(View):
    def get(self, request):
        return render(request, 'TextManage.html')

    def post(self, request,ttextmanageid):
        TextMange.objects.filter(ttextmanageid=ttextmanageid).delete()
        all_textmanages = TextMange.objects.all()
        return render(request, 'TextManage.html', {'all_textmanages': all_textmanages})


def textanalysis(request):
    all_textanalysis=WFreq.objects.all()
    return render(request,'TextAnalysis.html',{'all_textanalysis':all_textanalysis})


# class textanalysis(View):
#     def get(self,request):
#         return render(request,'PassageAnalysis.html')
#     def post(self,request):
#         all_textanalysis= WFreq.objects.all()
#         return render(request,'PassageAnalysis.html',{'all_textanalysis':all_textanalysis})


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








