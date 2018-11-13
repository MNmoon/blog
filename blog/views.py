# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

'''
def index(request):
    #添加两个变量，并给它们赋值
    sitename = 'Django中文网'
    url = 'www.django.cn'
    list=[
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    #把两个变量封装到上下文里
    context={
        'sitename':sitename,
        'url':url,
        'list':list,
    }
    # 把上下文传递到模板里
    return render(request,'index.html',context)
'''


def index(request):
    #对Article进行声明并实例化，然后生成对象allarticle(文章)
    allarticle = Article.objects.all()
    #把查询到的对象，封装到上下文
    context = {
        'allarticle': allarticle,
    }
    return render(request,'blog/index.html',context)



def list(request):
    pass