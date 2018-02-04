# coding:utf-8
import redis


class Config(object):
    SECRET_KEY = 'BSAKJDHFADSFJWBAJKD'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'

    # flask_session 配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # SESSION数据的有效性，单位秒


class DevelopmentConfig(Config):
    """开发模式配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False


config_map = {
    'develop': DevelopmentConfig,
    'product': ProductionConfig
}
