from django.shortcuts import render,HttpResponse
from TextManage.models import TextMange
from django.views import View


# Create your views here.
def TextManageView(request):
    all_textmanages = TextMange.objects.all()
    return render(request,'TextManage.html',{'all_textmanages': all_textmanages})

def textlist(request):
    all_textmanages =TextMange.objects.all()
    return render(request,'text_list.html',{'all_textmanages': all_textmanages})


class Upload(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):

        file = request.FILES.get('f1')
        # 获取文件名后缀
        suffix = file.name.split(".")[1]
        print("suffix: {}".format(suffix))
        # 判断后缀
        if 'pdf' == suffix or 'docx' == suffix or 'doc' == suffix:
            with open(file.name, 'wb') as f:
                for i in file:
                    f.write(i)
            global userid
            ret = TextMange.objects.create(pname=file.name,userid=userid)
            print(ret)
            # return render(request, 'usermanage/Main_1.html', {'userid': userid})
            return HttpResponse('ok')
        else:
            return HttpResponse('NO')

    def textadd(request):
        return render(request,'text_add.html')
