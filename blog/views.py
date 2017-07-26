from django.shortcuts import render
from django.http import HttpResponse

from .import models
# Create your views here. 创建页面
def index(request):
    # 1、加载响应
    # return HttpResponse('Hello world!')
    # 2、加载Html文件
    # 3、获取文章列表
    #  article = models.Article.objects.get(pk=1)
    # 4、获取所有的文章对象
    # 博客主页面开发
     articles = models.Article.objects.all()
     return render(request, 'blog/index.html', {'articles': articles})
 # 博客文章页面开发
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
# 博客撰写页面开发（一）
def edit_page(request):
    return render(request, 'blog/edit_page.html')
# 编辑响应函数
def edit_action(request):
    title = request.Post.get('title', 'TITLE')
    content = request.Post.get('content', 'CONTENT')
    models.Article.objects.create(title = title, content = content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

