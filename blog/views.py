from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 创建页面
def index(request):
    return HttpResponse('Hello world!')

