# coding:utf-8

from . import api
from ihome import db,models
from flask import current_app

# print ('demmo')


@api.route("/index")
def index():
    current_app.logger.error("error info")
    current_app.logger.warn("warn info")
    current_app.logger.info("info info")
    current_app.logger.debug("debug info")
    # print ('demmo2')
    return "index page"


# print ('demmo3')
