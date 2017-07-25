from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 创建页面
def index(request):
    # 1、加载响应
    # return HttpResponse('Hello world!')
    # 2、加载Html文件
     return render(request, 'blog/index.html')

