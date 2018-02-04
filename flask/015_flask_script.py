# coding:utf-8


# 脚本扩展
from flask import Flask
from flask_script import Manager  # 脚本启动命令,manager管理类

app = Flask(__name__)

# 创建manager管理类对象
manager = Manager(app)


@app.route('/')
def home():
    return '脚本文件运行'


if __name__ == '__main__':
    # app.run(port=5001)
    manager.run()