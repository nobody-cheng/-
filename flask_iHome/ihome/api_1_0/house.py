# coding:utf-8

from flask import current_app, request, jsonify, g, session
from ihome.api_1_0 import api
from ihome.utils.commons import login_required
from ihome.models import User
from ihome.utils.response_code import RET
from ihome import redis_store, constants, db
from ihome.models import Area, House, Facility, HouseImage, User, Order
from ihome.utils.image_storage import storage
import json


@api.route("/users/auth", methods=['GET'])
@login_required
def get_myhouse_auth():
    # 获取当前登陆账户
    user_id = g.user_id
    # 从数据库中查询是否实名认证
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询用户失败")

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg='无效操作')
    data = user.auth_to_dict()
    print (data)
    return jsonify(errno=RET.OK, errmsg='OK', data=user.auth_to_dict())


@api.route("/areas")
def get_area_info():
    """获取城区信息"""
    # 尝试从redis中读取数据
    try:
        resp_json = redis_store.get("area_info")
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            # redis有缓存数据
            current_app.logger.info("hit redis area_info")
            return resp_json, 200, {"Content-Type": "application/json"}

    # 查询数据库，读取城区信息
    try:
        area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    area_dict_li = []
    # 将对象转换为字典
    for area in area_li:
        area_dict_li.append(area.to_dict())

    # 将数据转换为json字符串
    resp_dict = dict(errno=RET.OK, errmsg="OK", data=area_dict_li)
    resp_json = json.dumps(resp_dict)

    # 将数据保存到redis中
    try:
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CACHE_EXPIRES, resp_json)
    except Exception as e:
        current_app.logger.error(e)

    return resp_json, 200, {"Content-Type": "application/json"}
