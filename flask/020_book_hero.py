# coding:utf-8
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

app = Flask(__name__)


class Config(object):
    # sqlalchemy设置连接数据
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/booktest"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFCATIONS = True
    SECRET_KEY = 'dksahfkjnadadfed'


app.config.from_object(Config)
db = SQLAlchemy(app)  # 创建db数据库sqlalchemy工具对象


class Author(db.Model):
    """定义模型类-作者"""
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64))
    au_book = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author:%s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32), unique=True)
    lead = db.Column(db.String(64))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return 'Book:%s,%s' % (self.info, self.lead)


# 创建表单类,用来添加信息
class Append(FlaskForm):
    au_info = StringField(label=u'作者', validators=[DataRequired(u'作者必填')])
    bk_info = StringField(label=u'书籍', validators=[DataRequired(u'书籍必填')])
    submit = SubmitField(label=u'添加')


@app.route('/index_book', methods=['GET', 'POST'])
def index():
    author = Author.query.all()
    book = Book.query.all()

    """
    创建表单对象,如果是post请求，前端发送了数据，
    flask会把数据在构造form对象的时候，存放到对象中
    """
    form = Append()
    # 判断form中的数据是否合理
    # 如果form中的数据完全满足所有的验证器，则返回真，否则返回假
    if form.validate_on_submit():
        # 获取表单信息
        wtf_au = form.au_info.data
        wtf_bk = form.bk_info.data
        # 把表单数据存入模型类
        db_au = Author(name=wtf_au)
        db_bk = Book(name=wtf_bk)
        # 提交会话
        db.session.add_all([db_au, db_bk])
        db.session.commit()
        # 添加数据后再次查询所有作者和书籍
        author = Author.query.all()
        book = Book.query.all()
        return render_template('index_book.html', author=author, book=book, form=form)

    else:
        if request.method == 'GET':
            render_template('index_book.html', author=author, book=book, form=form)

    return render_template('index_book.html', author=author, book=book, form=form)


# 删除作者
@app.route('/delete_author<id>')
def delete_author(id):
    # 精确查询需要删除的作者id
    au = Author.query.filter_by(id=id).first()
    print u'删除作者前'
    db.session.delete(au)
    print u'删除作者后'
    db.session.commit()
    return redirect(url_for('index'))


# 删除书籍
@app.route('/delete_book<id>')
def delete_book(id):
    bk = Book.query.filter_by(id=id).first()
    db.session.delete(bk)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 生成数据
    au_xi = Author(name='我吃西红柿', email='xihongshi@163.com')
    au_qian = Author(name='萧潜', email='xiaoqian@126.com')
    au_san = Author(name='唐家三少', email='sanshao@163.com')
    bk_xi = Book(info='吞噬星空', lead='罗峰')
    bk_xi2 = Book(info='寸芒', lead='李杨')
    bk_qian = Book(info='飘渺之旅', lead='李强')
    bk_san = Book(info='冰火魔厨', lead='融念冰')

    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()

    app.run(debug=True)
