# coding:utf-8
from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def index():
    # 1.使用元祖信息,返回自定义的响应信息
    #        响应体  状态码   响应头
    # return u'响应体', 400, [('key', 'value'), ('key2', 'value2')]
    # return u'响应体', '666 python', {"country": "china", "City": "sz"}

    # 2. 使用make_response 构造响应体信息
    resp = make_response(u'构造响应体')
    resp.status = '22 python'  # 设置响应状态码
    resp.headers['country'] = 'china'  # 设置响应头
    return resp


if __name__ == '__main__':
    app.run(debug=True)
