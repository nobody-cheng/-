# coding:utf-8
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response, request
from ihome.utils.response_code import RET
from ihome.models import User
from ihome.libs.yuntongxun.sms import CCP
import random


# Restful风格
# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>
@api.route('/image_codes/<image_code_id>')
def get_image_code(image_code_id):
    """
    获取图片验证码　
    :params: image_code_id 图片验证码编号
    :return: 验证码图片
    """
    # 获取参数
    # 检验参数
    # 业务逻辑处理
    # 生成验证码图片

    # 名字 真实文本 图片数据
    name, text, image_data = captcha.generate_captcha()

    # 将验证码真实值与编号保存到redis中, 设置有效期
    # redis：  字符串   列表  哈希   set(集合)  zset(有序集合)
    # "key": xxx
    # 使用哈希维护有效期的时候只能整体设置
    # "image_codes": {"id1":"abc", "":"", "":""} 哈希  hset("image_codes", "id1", "abc")  hget("image_codes", "id1")

    # 将验证码真实性和编号保存到redis
    try:                                   # 记录名字　　　　　　有效期　　　　　　　　　　　　　　　　记录值
        redis_store.setex('image_code_%s' % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg='保存图片验证码失败')
    # 返回图片
    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/jpg'
    # print ('text=====', text)
    return resp


@api.route("/sms_codes/<re(r'1[34578]\d{9}'):mobile>")
def get_sms_code(mobile):
    """获取短信验证码"""
    # 获取参数
    image_code = request.args.get('image_code')  # 用户填写的图片验证码的内容
    image_code_id = request.args.get('image_code_id')  # 图片验证码的编号
    print ('image_code_id==%s,image_code==%s' % (image_code_id, image_code))

    # 校验参数
    if not all([image_code_id, image_code]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 业务逻辑处理
    # 从redis中取得图片验证码
    try:
        real_image_code = redis_store.get('image_code_%s' % image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='redis数据库异常')
    # 判断图片验证码是否过期
    if real_image_code is None:
        return jsonify(errno=RET.NODATA, errmsg='图片验证失效')
    # 与用户填写验证码对比
    if real_image_code.lower() != image_code.lower():
        return jsonify(errno=RET.DATAERR, errmsg='图片验证码错误')

    # 获取验证码的频繁性，设置为６０秒
    # try:
    #     send_flag = redis_store.get('send_sms_code_%s' % mobile)
    # except Exception as e:
    #     current_app.logger.error(e)
    # else:
    #     if send_flag is not None:
    #         # 表示在60秒内之前有过发送的记录
    #         return jsonify(errno=RET.REQERR, errmsg='请求频繁，请稍后')

    # 判断手机号码是否存在
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
    else:
        # 手机号已存在
        if user is not None:
            return jsonify(errno=RET.DATAEXIST, errmsg='手机号已存在')
    # 若手机号不存在,则生成短信验证码
    sms_code = '%06d' % random.randint(0, 999999)
    # 保存真实的短信验证码
    try:
        redis_store.setex('sms_code_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存发送给这个手机号的记录,防止用户多次请求
        redis_store.setex('send_sms_code_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存短信验证码异常')

    # 发送短信
    try:
        ccp = CCP()                      # 手机号   验证码     有效期
        result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES / 60)], 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='发送异常')
    # 返回值
    if result == 0:
        # 发送成功
        return jsonify(errno=RET.OK, errmsg='发送成功')
    else:
        return jsonify(errno=RET.THIRDERR, errmsg='发送失败')
