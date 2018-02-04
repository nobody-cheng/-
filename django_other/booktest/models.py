from django.db import models

# Create your models here.


# 定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle = models.CharField(verbose_name='地区',max_length=30)  # 名称
    aParent = models.ForeignKey('self',verbose_name='上级地区',null=True,blank=True) # 父级

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle
    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

    def parent(self):
        if self.aParent:
            return self.aParent.atitle
        else:
            return '无'


class PicTest(models.Model):
    # 上传图片的物理路径：MEDIA_ROOT+upload_to+文件名
    pic = models.ImageField(upload_to='booktest')