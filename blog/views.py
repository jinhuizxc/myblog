from django.shortcuts import render
from django.http import HttpResponse

from .import models
# Create your views here. 创建页面
def index(request):
    # 1、加载响应
    # return HttpResponse('Hello world!')
    # 2、加载Html文件
     article = models.Article.objects.get(pk=1)
     return render(request, 'blog/index.html', {'article': article})

