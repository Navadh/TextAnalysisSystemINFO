from django.shortcuts import render
from TextManage.models import TextMange


# Create your views here.
def TextManageView(request):
    return render(request,'TextManage.html')