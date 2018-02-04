# coding:utf-8
from flask import Blueprint

# 1.创建蓝图对象
app_goods = Blueprint('goods', __name__)


@app_goods.route('/get_goods')
def get_goods():
    return 'get goods page'
