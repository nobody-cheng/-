# coding:utf-8

from flask import Flask
from orders import get_order
from users import register
from goods import app_goods
import cart

# 解决循环导入的办法,让一方推迟导入
app = Flask(__name__)

# 　为视图函数添加装饰器，将ｕｒｌ路径与视图函数绑定在一起
app.route('/get_orders')(get_order)
app.route('/register')(register)

# 注册蓝图 第一个参数 app_goods 是蓝图对象，url_prefix参数默认值是根路由，如果指定，会在蓝图注册的路由url中添加前缀。
app.register_blueprint(app_goods, url_prefix='/goods')
app.register_blueprint(cart.app_cart, url_prefix='/carts')


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    print (app.url_map)
    app.run(debug=True)
    # app.run()
