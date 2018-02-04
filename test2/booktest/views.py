from django.shortcuts import render, redirect
from .models import *
from django.db.models import F, Q, Sum
from datetime import date
from django.http import HttpResponse

from PIL import Image,ImageDraw,ImageFont
# Create your views here.

"""
模型类的成员:
    类属性:管理器manager,默认是objects
    对象属性:str() , save() , delete()
"""

def index(request):
    # 查询所有的图书信息
    # blist = BookInfo.objects.all()
    # 自定义的管理器
    # blist = BookInfo.books.all()

    # 查询编号为1的图书
    # blist = BookInfo.books.filter(id=1)

    # 查询书名包含‘传’的图书
    # blist = BookInfo.books.filter(btitle__contains='传')

    # 查询书名以‘部’结尾的图书
    # blist = BookInfo.books.filter(btitle__endswith='部')

    # 查询书名不为空的图书
    # blist = BookInfo.books.filter(btitle__isnull=False)

    # 查询编号为1或3或5的图书
    # blist = BookInfo.books.filter(pk__in=[1, 3, 5])

    # 查询编号大于3的图书
    # blist = BookInfo.books.filter(id__gt=3)

    # 查询编号不等于3的图书
    # blist = BookInfo.books.exclude(id=3)

    # 查询1980年发表的图书
    # blist = BookInfo.books.filter(bpub_date__year=1980)

    # 查询1980年1月1日后发表的图书
    # blist = BookInfo.books.filter(bpub_date__gt=date(1980,1,1))

    # 两个属性比较 F对象
    # 查询阅读量大于评论量的图书
    # blist = BookInfo.books.filter(bread__gte=F('bcommet'))

    # # 查询阅读量大于评论量的图书
    # blist = BookInfo.books.filter(bread__gt=F('bcommet')*2)

    # Q对象:多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字
    # 查询阅读量大于20，并且编号小于3的图书
    # blist = BookInfo.books.filter(bread__gt=20,id__lt=3)
    # blist = BookInfo.books.filter(breat__gt=20).filter(id__lt=3)

    # 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
    # blist = BookInfo.books.filter(Q(bread__gt=20) | Q(pk__lt=3))

    # 查询编号不等于3的图书
    # blist = BookInfo.books.filter(~Q(pk=3))

    # 查询图书，要求图书中英雄的描述包含‘八’
    # blist = BookInfo.books.filter(heroinfo__hcontent__contains='八')
    # # 查询书名为“天龙八部”的所有英雄
    # hlist = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    #
    # # 查询图书的总阅读量
    # reads = BookInfo.books.aggregate(Sum('bread'))
    # # {'bread__sum': 126}
    # print(reads)
    # context = {'blist': blist, 'hlist': hlist, 'reads': reads}


    # 查询性别为男的英雄
    # hlist = HeroInfo.objects.filter(hgender=True)
    # 查询姓黄的男性英雄
    hlist = HeroInfo.objects.filter(hname__startswith='黄',hgender=True)
    # 查询图书名为“天龙八部”的英雄
    # hlist = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # 查询编号小于5或性别为女的英雄
    hlist = HeroInfo.objects.filter(Q(pk__lt=5)|Q(hgender=False))
    context = {'hlist':hlist}
    return render(request, 'booktest/index.html', context)


def add(request):
    # 创建图书对象
    # book = BookInfo()
    # book.btitle = 'abc'
    # book.bpub_date = date(2001,2,2)
    # book.save()

    # 调用管理器的方法创建对象
    book = BookInfo.books.create_book('传图书', date(2017,2,22))
    # 转向首页 重定向redirrect
    return redirect('/')


def delete(request, bid):
    # book = BookInfo.objects.get(pk=bid)
    book = BookInfo.books.get(pk=bid)
    # 物理删除
    # book.delete()

    # 逻辑删除
    book.isDelete = True

    book.save()
    return redirect('/')

def area(request):
    # 查询名称为梅州市的地区对象
    city = AreaInfo.objects.filter(atitle='梅州市')[0]
    # 获取梅州市对应的省份
    sheng = city.aParent
    # 获取广州市的区县
    qx = city.areainfo_set.all()

    context = {'city': city,'sheng':sheng,'qx':qx}
    return render(request,'booktest/area.html',context)

def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量,用于画面的背景色,宽,高
    bgcolor = (random.randrange(20,100),random.randrange(20,100),255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width,height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    # 定义验证码的备选值
    str1 = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str1[random.randrange(0,len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('FreeMono.ttf',23)
    # 构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    # 绘制4个字
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor)
    draw.text((25,2),rand_str[1],font=font,fill=fontcolor)
    draw.text((50,2),rand_str[2],font=font,fill=fontcolor)
    draw.text((75,2),rand_str[3],font=font,fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session,用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作
    from io import BytesIO
    buf = BytesIO()

    # 将图片保存在内存中,文件类型为png
    im.save(buf,'png')
    # 将内存中的图片数据返回给客户端,MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')

def verify_show(request):
    return render(request, 'booktest/verify_show.html')