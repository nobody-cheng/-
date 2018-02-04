# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python04"

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    """角色表"""
    __tablename__ = 'tbl_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    users = db.relationship('User', backref='role')  # 关联从上层考虑,关系模型类


# 表名的常见规范
# ihome -> ih_user   数据库名缩写_表名
# tbl_user  tbl_表名
# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = 'tbl_user'  # 指明数据库的表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键,会默认为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 关联从底层考虑


if __name__ == '__main__':
    # app.run(port=5001)
    db.drop_all()  # 清除数据库中的所有数据,只在第一次使用
    db.create_all()  # 创建所有的表

    role1 = Role(name='admin')  # 创建对象
    db.session.add(role1)  # session记录对象任务
    db.session.commit()  # 提交任务到数据库中

    role2 = Role(name='stuff')
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    # 一次保存多条数据
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()

"""
两个类User和Role均继承自db.Model
__tablename__用来指定表名称
db.Coumn函数指定了数据库中字段类型,是否主键primary_key,是否唯一unique,是否加索引index,是否可以为空nullable=True等

在User表中添加了一个role_id变量,数据类型db.Integer,第二个参数指定外键是哪个表中哪个id,其类型要与关联的类型相同,外键定义在多的一方

在Role表中users = db.Relationship('User',backref='role')
1.添加到Relo模型中的users属性代表这个关系面向对象,对于Role类的实例,其users属性将返回与角色相关联的用户组成表
2.db.Relationship()第一个参数表明这个关系的另外一端是哪一个模型类,若模型类尚未定义,用字符串形式指定
3.db.Relationship()第二个参数backref,将向User类中添加一个Role属性,从而定义反向关系.这一个属性可替代role_id访问Role模型,此时获取的是模型对象,而不是外键的值

"""
