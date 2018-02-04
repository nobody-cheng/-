from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from .models import AreaInfo
# Create your views here.

def index(request):
    print('~~~~~~~index')
    return render(request, 'booktest/index.html')


def pic1(request):
    return render(request,'booktest/pic1.html')
def pic2(request):
    # 接收请求的文件
    p1=request.FILES.get('pic')
    # print(type(p1))
    print(p1.content_type)
    # 接收表单数据
    pname=request.POST.get('pname')
    # 保存文件
    storage=FileSystemStorage()
    # 保存路径：MEDIA_ROOT+'booktest/%s'%p1.name
    fname=storage.save('booktest/%s'%p1.name,p1)
    # 存入表中
    pic=PicTest()
    pic.pic=fname
    pic.save()

    return HttpResponse('ok')

def page_test(request, pIndex): # pIndex表示当前要显示的页码
    # 查询所有的地区信息
    list1 = AreaInfo.objects.filter(aParent__isnull = True)
    # 将地区信息按一页10条进行分页
    # 方法init(列表,int)：返回分页对象，参数为列表数据，每面数据的条数
    p = Paginator(list1, 10)
    # 如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写代码
    if pIndex == '':
        pIndex = '1'
    # 通过url匹配的参数都是字符串类型，转换成int类型
    pIndex = int(pIndex)
    # 获取第pIndex页的数据
    # 方法page(m)：返回Page对象，表示第m页的数据，下标以1开始
    list2 = p.page(pIndex)
    # 获取所有的页码信息
    plist = p.page_range
    # 将当前页码、当前页的数据，页码信息传递到模板中
    return render(request, 'booktest/page_test.html', {'list': list2, 'plist': plist, 'pIndex': pIndex})