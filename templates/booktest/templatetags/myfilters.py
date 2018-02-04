from django.template import Library
"""
自定义过滤器:
1.引入library;
2.创建对象,名称必须为register
3.为函数加装饰器register.filter
"""

register=Library()

@register.filter
def mod(num):
    return num%2

@register.filter
def mod3(num1,num2):
    return num1%num2