# coding:utf-8
from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# @app.route('/goods/<int:goods_id>')
@app.route('/goods/<goods_id>')  # 不加转换器类型,默认是普通字符串规则(除了/的字符)
def goods_detail(goods_id):
    return '动态路由%s' % goods_id


# 1.定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map, ):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[3578]\d{9}'


app.url_map.converters['mobile'] = MobileConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 5.调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 4.将正则表达式的参数保存到对象的属性中,flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex  # regex是从BaseConverter继承

    def to_python(self, value):
        print("to_python方法被调用")
        # return 'to_python'
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        """使用url_for的方法的时候被调用"""
        print("to_url方法被调用")
        return "15822222222"
        # return value


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters['re'] = RegexConverter  # 把RegexConverter类存入去


# @app.route('/send/<mobile:mobile_num>')
# def send_sms(mobile_num):
#     return 'send sms to %s' % mobile_num


# 3.进行使用转换器
# 127.0.0.1:5000/send/18612345678
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_msg(mobile):
    return 'send msg to %s' % mobile


@app.route('/index')
def index():
    url = url_for('send_msg', mobile=13888888888)
    # url=/send/13888888888
    return redirect(url)


@app.route("/call/<re(r''):tel>")
def call_tel(tel):
    pass


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
