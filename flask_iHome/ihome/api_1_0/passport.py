# coding:utf-8

from . import api
from flask import request, jsonify, current_app, session
from ihome.utils.response_code import RET
from ihome import redis_store, db, constants
from ihome.models import User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import re


@api.route("/users", methods=["POST"])
def register():
    """注册
    请求的参数： 手机号、短信验证码、密码、确认密码
    参数格式：json
    """
    # 获取请求的json数据，返回字典
    req_dict = request.get_json()

    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")
    password2 = req_dict.get("password2")

    # 校验参数
    if not all([mobile, sms_code, password, password2]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    # 判断手机号格式
    if not re.match(r"1[34578]\d{9}", mobile):
        # 表示格式不对
        return jsonify(errno=RET.PARAMERR, errmsg="手机号格式错误")

    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmsg="两次密码不一致")

    # 从redis中取出短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="读取真实短信验证码异常")

    # 判断短信验证码是否过期
    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmsg="短信验证码失效")

    # 删除redis中的短信验证码，防止重复使用校验
    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 判断用户填写短信验证码的正确性
    if real_sms_code != sms_code:
        return jsonify(errno=RET.DATAERR, errmsg="短信验证码错误")

    # 判断用户的手机号是否注册过
    # 保存用户的注册数据到数据库中
    user = User(name="", mobile=mobile)
    # user.generate_password_hash(password)

    user.password = password  # 设置属性

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # 数据库操作错误后的回滚
        db.session.rollback()
        # 表示手机号出现了重复值，即手机号已注册过
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")
    except Exception as e:
        db.session.rollback()
        # 表示手机号出现了重复值，即手机号已注册过
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据库异常")

    # 保存登录状态到session中
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id

    # 返回结果
    return jsonify(errno=RET.OK, errmsg="注册成功")


"""
登陆,号码,密码 post请求得到和数据库对比
"""


@api.route('/sessions', methods=['POST'])
def login():
    """登陆"""
    # 获取登陆参数
    print (u'登陆状态')

    req_dict = request.get_json()
    mobile = req_dict.get('mobile')
    password = req_dict.get('password')
    print ('req_dict', req_dict)
    print ('mobile', mobile)
    print ('password', password)
    # 校验参数
    # 参数完整的校验
    print (u'开始校验参数')
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号或者密码未填写')

    print (u'校验手机号的格式')
    # 手机号的格式
    if not re.match(r"1[34578]\d{9}", mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机格式错误')

    # 判断错误次数是否超过限制，如果超过限制，则返回
    # redis记录： "access_nums_请求的ip": "次数"
    # 号码符合格式,得到用户ip地址
    user_ip = request.remote_addr
    try:
        access_nums = redis_store.get('access_unm_%s' % user_ip)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) >= constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(errno=RET.REQERR, errmsg='错误次数过多,请稍后再试')

    print (u'从数据库查询用户数据')
    # 从数据库中根据手机号查询用户的数据对象
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询用户失败')

    print (u'密码校验')
    # 用数据库的密码与用户填写的密码进行对比验证
    if user is None or not user.check_password(password):
        # 验证失败，记录错误次数
        try:
            # redis的incr可以对字符串类型的数字数据进行加一操作，如果数据一开始不存在，则会初始化为1
            redis_store.incr('access_num_%s' % user_ip)
            redis_store.expire('access_num_%s' % user_ip, constants.LOGIN_ERROR_FORBID_TIME)  # 设置有效期
        except Exception as e:
            current_app.logger.error(e)
        return jsonify(errno=RET.LOGINERR, errmsg='用户名或者密码错误')
    print (u'登陆成功')
    # 如果验证相同成功，保存登录状态， 在session中
    session['mobile'] = user.mobile
    session['name'] = user.name
    # session['password'] = user.password
    session['user_id'] = user.id
    return jsonify(errno=RET.OK, errmsg='登陆成功')


@api.route('/session', methods=['GET'])
def check_login():
    """检查用户登陆状态"""
    name = session.get('name')
    if name is None:
        return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')
    else:
        """用户已登陆"""
        return jsonify(errno=RET.OK, errmsg='用户已登陆', data={'name': name})


@api.route('/session', methods=['DELETE'])
def logout():
    """退出登陆"""
    # 清除session
    csrf_token = session.get("csrf_token")
    session.clear()
    session["csrf_token"] = csrf_token
    return jsonify(errno=RET.OK, errmsg='OK')