# coding:utf-8

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
import functools
from ihome.utils.response_code import RET


# 定义正则转换器
class ReConverter(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        super(ReConverter, self).__init__(url_map)
        self.regex = regex


# 定义是否登陆状态的装饰器
def login_required(view_func):
    """wraps函数的作用将wapper内层函数的属性设置为被装饰函数view_func的属性"""

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        # 判断用户是否登陆
        if user_id is not None:
            # 用户登陆,执行视图函数
            # 将user_id保存到g对象中,在视图函数中可以通过g对象获取数据
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 未登录,返回未登录信息
            return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')

    return wrapper
