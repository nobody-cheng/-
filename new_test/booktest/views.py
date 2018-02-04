from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    # context = {'title1': 'hello django', 'list1': range(10)}
    # return HttpResponse('index')
    context = {'title1': 'hello django', 'list1': range(10)}
    return render(request, 'index.html', context)


# 列出所有的图书信息
def book(request):
    # 查询所有的图书
    blist = BookInfo.objects.all()
    # 构造上下文
    context = {'blist1': blist}
    # 调用模板
    return render(request, 'book.html', context)


# 根据图书的编号查询所有的英雄信息
def hero(request, bid):
    # 根据编号查询图书对象
    b = BookInfo.objects.get(pk = bid)
    # 找到对应的英雄
    # 关系字段定义在hero，django会在book中创建一个熟悉，名为heroinfo_set
    hlist = b.heroinfo_set.all()
    # 构造上下文
    context = {'hlist': hlist}
    # 调用模板
    return render(request, 'hero.html', context)