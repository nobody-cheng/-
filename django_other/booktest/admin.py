from django.contrib import admin
from .models import *
# Register your models here.


class AreainfoInline(admin.StackedInline):
    model = AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    # 列表页面的选项
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top = True
    list_display = ['id', 'atitle', 'aParent', 'title', 'parent']
    list_filter = ['atitle']
    search_fields = ['atitle']

    # 编辑页选项
    fieldsets = [
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']}),
    ]
    # 关联选项
    inlines = [AreainfoInline]


# 注册
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)