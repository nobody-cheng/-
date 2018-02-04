# coding:utf-8

# 图片验证码的redis有效期
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期, 单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔, 单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 多次登陆失败后的时间间隔, 单位：秒
LOGIN_ERROR_FORBID_TIME = 600

# 登录错误尝试次数
LOGIN_ERROR_MAX_TIMES = 5

# 七牛的域名
QINIU_URL_DOMAIN = "http://p060nopso.bkt.clouddn.com/"
# p060nopso.bkt.clouddn.com


# 城区信息的缓存时间, 单位：秒
AREA_INFO_REDIS_CACHE_EXPIRES = 7200
