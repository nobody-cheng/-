# coding:utf-8
from flask import Flask, redirect, url_for

app = Flask(__name__)

# 配置参数的使用方法
# 1.使用配置文件
app.config.from_pyfile('config.cfg')


@app.route('/')
def index():
    return 'hello index'


# 通过methods限定访问方式
@app.route('/post_only', methods=['GET', 'POST'])
def post_only():
    return 'post only page'


# # 相同的路由,按照顺序找到第一个
# @app.route('/hello')
# def hello():
#     return 'hello--1'
# @app.route('/hello')
# def hello_2():
#     return 'hello--1'

@app.route('/hello', methods=['POST'])
def hello():
    return '同一路由装饰多个视图函数--POST'


@app.route('/hello', methods=['GET'])
def hello_2():
    return '同一路由装饰多个视图函数--GET'


# 同一视图多个路由装饰器
@app.route('/hi')
@app.route('/hi2')
def hi():
    return '同一视图多个路由装饰器'


@app.route('/login')
def longin():
    # 使用url_for的函数,通过视图函数的名字找到视图对应的url路径
    url = url_for('index')  # url_for操作对象是视图函数
    return redirect(url)


@app.route('/register')
def register():
    url = url_for('index')
    return redirect(url)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
