# coding:utf-8
from flask import Flask, request, abort, Response, make_response, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    # a=1 /0
    print ('index  执行')
    return 'index'


@app.route('/hello')
def hello():
    print ('hello')
    return 'hello'


@app.before_first_request
def handle_before_first_request():
    # 第一次请求处理之前先被执行
    print ('before_firest_request 执行')


@app.before_request
def handle_before_request():
    # 每次请求前都被执行
    print ('before_request  执行')


@app.after_request
def handle_after_request(response):
    # 每次请求之后执行,前提是视图函数没有出现异常
    print ('handle_after_request 执行')
    return response


@app.teardown_request
def handle_teardown_request(response):
    # 每次请求后执行,无论视图函数是否出现异常,均执行,在生产环境(非调试环境下)工作运行
    path = request.path
    if path == url_for('index'):
        print ('在请求钩子中判断请求的视图逻辑: index')
    elif path == url_for('hello'):
        print ('在请求钩子中判断请求的视图逻辑: hello')
    print ('teardown_request 执行')
    return response


if __name__ == '__main__':
    app.run(port=5001)
