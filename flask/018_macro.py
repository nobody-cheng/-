# coding:utf-8
from flask import Flask, render_template, flash

app = Flask(__name__)

flag = True
app.config['SECRET_KEY'] = 'HSDKLNAFJBSDAKLJ'


@app.route('/macro')
def macro():
    if flag:
        # 添加闪现信息
        flash('hello1')
        flash('hello2')
        flash('hello3')
        flash('hello4')
        global flag
        flag = False
    return render_template('macro.html')


if __name__ == '__main__':
    app.run(port=5001)
