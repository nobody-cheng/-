# coding:utf-8
from flask import Flask, request, session
import json

app = Flask(__name__)
# flask的session需要用到的秘钥字符
app.config['SECRET_KEY'] = 'SDAKLHFKLADSHKJKHJL'


@app.route('/login')
def login():
    # 设置session数据
    session['name'] = 'zhangsan'
    session['mobile'] = '12222222222'
    return u'登陆成功'


@app.route('/index')
def index():
    # 获取session数据
    name = session.get('name')
    mobile = session.get(('mobile'))
    return '%s %s' % (name, mobile)


if __name__ == '__main__':
    app.run(debug=True)
