# coding:utf-8
from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HSADLKJFGDS'  # CSRF


class RegisterForm(FlaskForm):
    """
    自定义的注册表单模型类
    validators=[]  验证器
    DataRequired()  保证输入框有数据
    EqualTo()  比较两个字段的值，常用于比较两次密码输入
    """
    name = StringField(label=u'用户名', validators=[DataRequired(u'用户名不能为空')])
    password = PasswordField(label=u'请输入密码', validators=[DataRequired(u'密码不能为空'),
                                                         Length(6, 12, u'长度必须在6-12字符之间')])
    password2 = PasswordField(label=u'请再次输入密码', validators=[DataRequired(u'密码不能为空'),
                                                            EqualTo('password', u'两次密码不一致')])
    mobile = IntegerField(label=u'联系号码', validators=[DataRequired(u'联系号码不能为空')])

    submit = SubmitField(label=u'提交')


@app.route('/register', methods=['get', 'POST'])
def register():
    """
    创建表单对象,如果是post请求，前端发送了数据，
    flask会把数据在构造form对象的时候，存放到对象中
    """
    form = RegisterForm()
    # 判断form中的数据是否合理
    # 如果form中的数据完全满足所有的验证器，则返回真，否则返回假
    if form.validate_on_submit():
        # 表示验证合格
        # 提取数据
        uname = form.name.data
        # uname = form.name
        pwd = form.password.data
        pwd2 = form.password2.data
        phone = form.mobile.data

        session['name'] = uname
        session['mobile'] = phone
        print(uname, pwd, pwd2, phone)
        return redirect(url_for("home"))

    return render_template('register.html', form=form)


@app.route('/home')
def home():
    uname = session.get('name', '')
    phone = session.get('mobile', '')

    return '%s %s' % (uname, phone)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
