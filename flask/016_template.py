# coding:utf-8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    data = {
        'name': 'zhangcheng',
        'age': 22,
        'my_dict': {'a': '1', 'b': '2'},
        'my_list': [3, 4, 5, 6, 7, 8],
        'int': 2
    }
    return render_template('home.html', **data)


def my_list_step_2(li):
    return li[::2]


app.add_template_filter(my_list_step_2, 'li2')


@app.template_filter('li3')
def my_list_step_3(li):
    return li[::3]


if __name__ == '__main__':
    app.run(debug=True, port=5001)
