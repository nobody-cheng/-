# coding:utf-8
from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # name = request.form.get()
    # pwd = request.form.get()
    name = ""
    pwd = ""
    if name != 'xidada' or pwd != 'qwert':
        # 使用abort函数可以立即终止视图函数执行,并返回给前端特定的信息
        # 1.传递状态码信息,必须符合http协议状态码,常用
        abort(404)

        # # 2.传递响应体信息
        # resp = Response("登陆失败")
        # abort(resp)
    return '登陆成功'


# 自定义异常处理
@app.errorhandler(404)
def handle_404_error(error):
    # 返回到页面显示
    return u'出现404错误,错误信息:%s' % error


if __name__ == '__main__':
    app.run(debug=True)
