# coding:utf-8

from . import api
from ihome.utils.commons import login_required
from flask import g, request, jsonify, current_app, session
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.models import User
from ihome import db, constants


@api.route("/users/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """"上传用户头像
    参数　图片　用户id
    """
    print ('获取头像')
    user_id = g.user_id  # 装饰器中已有user_id 存入g对象
    # 获取头像
    image_file = request.files.get("avatar")
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg='头像未上传')

    image_data = image_file.read()  # 二进制
    print ('###################', image_data)
    # 上传到七牛服务器中
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='头像上传失败')
    print ('头像上传成功')

    # 上传成功，保存文件名到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存头像失败')

    avatar_url = constants.QINIU_URL_DOMAIN + file_name
    # 保存成功
    return jsonify(errno=RET.OK, errmsg='保存成功', data={'avatar_url': avatar_url})


@api.route('/users/name', methods=["PUT"])
@login_required
def change_user_name():
    """保存,修改用户名"""
    # 当前登陆用户
    user_id = g.user_id

    # 获取设置用户名
    request_dict = request.get_json()
    name = request_dict.get('name')  # 用户设置id名
    print ('=====获取设置用户名======', name)

    # 校验参数
    if name is None:
        return jsonify(errno=RET.PARAMERR, errmsg='用户名为空')

    try:
        user = User.query.filter_by(id=user_id).first()
        user_db_name = User.query.filter_by(name=name).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库查询失败")

    if user:
        """数据库查询到user"""
        if user_db_name:
            print ("重复名字")
            return jsonify(errno=RET.DATAEXIST, errmsg="改用户名已被占用")
        else:
            user.name = name
            print ("修改用户名")

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="修改用户名失败")

        # 修改session数据中的name字段
        session['name'] = name
        return jsonify(errno=RET.OK, errmsg='OK')

    return jsonify(errno=RET.DBERR, errmsg="数据库查询失败")


@api.route("/users", methods=["GET"])
@login_required
def get_users_profile():
    """查询个人信息"""
    # 用户名,手机号,头像url,用户id
    user_id = g.user_id
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询个人信息失败')

    if user is None:
        return jsonify(errno=RET.DBERR, errmsg='未查询到个人信息')
    return jsonify(errno=RET.OK, errmsg='OK', data=user.to_dict())


@api.route("/users/auth", methods=['POST'])
@login_required
def set_user_auth():
    """设置实名信息"""
    print ("$$$$$$$$$$$$$$$$$$$$$$设置实名信息")
    user_id = g.user_id
    request_dict = request.get_json()

    if request_dict is None:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    real_name = request_dict.get('real_name')
    id_card = request_dict.get('id_card')

    if not all([real_name, id_card]):
        return jsonify(errrno=RET.PARAMERR, errmsg='参数错误')

    # 保存用户姓名及身份证号
    try:
        User.query.filter_by(id=user_id, real_name=None, id_card=None, ).update(
            {'real_name': real_name, 'id_card': id_card})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logeger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存实名信息失败')
    print ("@@@@@@@@@@@@@@@@@@@@@@@")
    return jsonify(errno=RET.OK, errrmsg='OK')


@api.route("/useres", methods=["GET"])
@login_required
def get_user_auth():
    """查询用户的实名认证信息"""
    print ("----------------")

    user_id = g.user_id

    # 数据库中查询
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询用户失败')

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg='无效操作')
    data = user.auth_to_dict()
    print (data)
    return jsonify(errno=RET.OK, errmsg='OK', data=user.auth_to_dict())
