# coding:utf-8
from flask import Flask

app = Flask(__name__)


# 配置参数的使用方法

# 1.使用配置文件
# app.config.from_pyfile('config.cfg')

# # 2.使用对象配置参数
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)


# 3.直接操作config的字典对象
app.config['DEBUG'] = True


@app.route('/')
def index():
    a = 1 / 0
    return '<h1>你好</h1>'


if __name__ == '__main__':
    app.run()
