from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')

# GET请求
def get1(request):
    return render(request, 'booktest/get1.html')
# 一键一值
def get2(request):
    dict = request.GET
    a = dict.get('a')
    b = dict.get('b')
    c = dict.get('c')

    context = {'a':a,'b':b,'c':c}
    return render(request, 'booktest/get2.html', context)
# 一键多值
def get3(request):
    dict = request.GET
    a = dict.getlist('a')
    b = dict.getlist('b')
    c = dict.getlist('c')

    context = {'a':a,'b':b,'c':c}
    return render(request, 'booktest/get3.html', context)


def post1(request):
    return render(request, 'booktest/post1.html')
def post2(request):
    dict = request.POST
    uname = dict.get('uname')
    upwd = dict.get('upwd')
    ugender = dict.get('ugender')
    uhobby = dict.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request, 'booktest/post2.html', context)


def red1(request):
    return redirect('/')

def json1(request):
    # json,当页面需要局部刷新的时候使用
    return render(request, 'booktest/json1.html')
def json2(request):
    # 接收请求过来的数据
    title = request.GET.get('title')
    # 进行处理
    s1 = '%s django' % title
    return JsonResponse({'h1': s1})

def cookie_set(request):
    # response = HttpResponse('<h1>设置cookie,查看响应报文头</h1>')
    response = HttpResponse('ok')
    # set_cookie('键','值',expires=过期时间)
    response.set_cookie('h1','django',expires=60*60*24*7)
    return response

def cookic_get(request):
    h1 = request.COOKIES.get('h1')
    return HttpResponse(h1)

def session_test(request):
    h1 = '你好啊'
    # 写
    request.session['h1'] = 'hello'

    return HttpResponse(h1)