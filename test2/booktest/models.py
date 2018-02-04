from django.db import models

# Create your models here.

"""
自定义管理器:
管理器是类属性
用途一:更改原始查询集
用途二:为模型类扩展类方法
"""


class BookInfoManager(models.Manager):
    def getj_queryset(self):
        return super().get_queryset().filter(isDelete=False)

    def create_book(self,btitle,bpup_date):
        """
        为模型类扩展类方法--创建爱一个图书对象
        self.model表示当前管理器对应的模型类，此处为BookInfo
        此处BookInfo就是self.model
        book为对象
        """
        book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpup_date
        book.save()
        return book


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcommet = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    class Meta:  # 元 信息类 指定写法
        db_table = 'bookinfo'# 指定表的名称

        # 每个类默认都有一个属性objects，表示Manager对象，负责查询
        # 如果创建一个属性则objects属性将不存在
        # 管理器Manager是ORM的核心，负责ORM的调用
        # books = models.Manager()
    books = BookInfoManager()


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcontent = models.CharField(max_length=100)  # 英雄描述信息
    hbook = models.ForeignKey('BookInfo')  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型中
    # hbook代表BookInfo对象
    # hbook_id是django生成的属性,表示BookInfo对象的id属性


#定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle=models.CharField(max_length=30)#名称
    aParent=models.ForeignKey('self',null=True,blank=True)#关系
