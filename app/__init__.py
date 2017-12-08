# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:18
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from flask import Flask
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint


app = Flask(__name__)
app.debug = True
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

