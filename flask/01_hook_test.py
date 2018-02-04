# coding:utf-8
from flask import Flask
from flask import request

app = Flask(__name__,
            static_url_path='/static',  # static_url_path='/python',  # 访问静态资源的url前缀,默认值是static
            static_folder='static',  # 静态文件的目录,默认就是static
            template_folder='templates',  # 模板文件的目录,默认是templates
            )


@app.route('/index')
def index():
    return 'hello index22'


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


# @app.before_request
@app.route('/login', methods=['GET'])
def login():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">登陆</button></p>
              </form>'''


@app.route('/login', methods=['POST'])
def login_handle():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    # print(app.url_map)
    # 启动flask程序
    app.run(port=5001)
