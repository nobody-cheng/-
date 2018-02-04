from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from PIL import Image, ImageDraw, ImageFont
# Create your views here.


def index(request):
    '''
    首先到项目目录下的templates下找模板文件，
    如果不存在，则到应用目录下的templates下找模板文件
    如果没有特别说明，一般将模板放在项目目录下
    '''
    return render(request, 'booktest/index.html')


def bianliang(request):
    book = BookInfo.objects.all()
    dict = {'title': '字典键值'}
    book.btitle = '对象属性'
    context = {'dict': dict,'book': book}
    return render(request, 'booktest/bianliang.html', context)


def biaoqian(request):
    list = BookInfo.objects.all()
    context = {'list': list}
    return render(request, 'booktest/biaoqian.html', context)


def glq(request):
    blist = BookInfo.objects.all()
    context = {'blist': blist}
    return render(request, 'booktest/glq.html', context)


def list(request):
    """
    1.继承,相同的内容定义在父模板
    2.父模板中可以预留多个区域,但名称不可相同
    {% block head %}{% endblock head %}\{% block body %}{% endblock body %}
    3.视图通过上下文传递数据,可在父模板中访问
    4.子类继承的时候需要引入{% extends '父类模板名称.html' %}
    """
    content = {'title': 'hello django'}
    return render(request, 'booktest/list.html', content)


def zhuanyi(request):
    """
    模板对上下文传递的字符串进行输出时，会对以下字符自动转义
    <,>,'',"",&\\\&lt;&gt;&#39;&quot;&amp;
    转义后标记代码不会被直接解释执行，而是被直接呈现，防止客户端通过嵌入js代码攻击网站
    过滤器safe：禁用转义,可以解释执行
    """
    context = {'text': '<h1>hello world</h1>'}
    return render(request, 'booktest/zhuanyi.html', context)


def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0qwertyuiopasdfghjklzxcvbnm'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    #内存文件操作(python2)
    #import cStringIO
    #buf = cStringIO.StringIO()

    #内存文件操作(python3)
    from io import BytesIO
    buf = BytesIO()

    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def yzm1(request):
    # 在页面显示文本框和验证码
    return render(request, 'booktest/yzm1.html')
def yzm2(request):
    # 进行判断
    yzm = request.POST.get('yzm')
    if yzm == request.session.get('verifycode'):
        return HttpResponse('验证码正确')
    else:
        return HttpResponse('验证码有误')