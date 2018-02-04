# coding:utf-8
from flask import Flask, request, abort, Response, make_response
import json

app = Flask(__name__)


@app.route('/set_cookie')
def set_cookie():
    # 构造一个对象
    resp = make_response('success')
    # 设置cookie,默认有效期是临时cookie
    resp.set_cookie('pwd', '123456')
    resp.set_cookie('pwd2', 'rtyhjk')
    resp.set_cookie('pwd3', 'rt0986', max_age=3600)
    resp.headers["Set-Cookie"] = 'pwd4=qqqqq; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/'
    return resp


@app.route('/get_cookie')
def get_cookie():
    cookie1 = request.cookies.get('pwd')
    return cookie1


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('del success')
    resp.delete_cookie('pwd2')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
