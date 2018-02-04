from django.db import models

# Create your models here.

# 模型类可以与数据库进行交互，进行crud操作，编写面向对象的代码就可以完成，不需要编写sql语句
# 一个类与一张表对应


class BookInfo(models.Model):
    # 图书名称，与表中的字段对应
    btitle = models.CharField(max_length=20)
    # 发布日期
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


# 英雄类
class HeroInfo(models.Model):
    # 姓名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField()
    # 简介
    hcontent = models.CharField(max_length=100)
    # 对 应的图书
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname