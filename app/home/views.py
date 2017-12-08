# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from app.home import home



@home.route('/')
def index():
    return '<h1 style="color:green">this is home</h1>'
