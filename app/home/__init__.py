# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:19
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from flask import Blueprint

home = Blueprint('home', __name__)

import app.home.views

