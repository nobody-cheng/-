# coding:utf-8
from flask import Flask, request

app = Flask(__name__)


class Foo(object):
    def __enter__(self):
        print('进入with语句的时候被with调用')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('离开with语句的时候被with调用')
        print('exc_type--%s' % exc_type)
        print('exc_val--%s' % exc_val)
        print('exc_tb--%s' % exc_tb)


with Foo() as foo:
    print('with用法')
    a = 1 / 0
    print('end')

if __name__ == '__main__':
    app.run(debug=True)

# with 构造请求上下文,“请求上下文”是一个上下文对象,实现__enter__和__exit__方法