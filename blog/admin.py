# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Category, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category','title','user','created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    list_display_links = ('title','category')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')
