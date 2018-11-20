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
    allarticle = Article.objects.all().order_by('-id')[0:10]
    #把查询到的对象，封装到上下文
    context = {
        'allarticle': allarticle,
    }
    return render(request,'blog/index.html',context)


#文章列表
def list(request,lid):
    list = Article.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    allcategory = Category.objects.all()#导航所有分类
    return render(request, 'list.html', locals())


def show(request,sid):
    show = Article.objects.get(id=sid)#查询指定ID的文章 因为获取的是单个对象，所以用get方法
    allcategory = Category.objects.all()#导航上的分类
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    #我们先通过show.views查询到当前浏览数，然后对这个数进行加1操作，意思是每访问一次页面（视图函数），就进行加1操作。然后再通过show.save()进行保存
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())