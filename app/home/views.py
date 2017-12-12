# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from app.home import home
from flask import render_template, redirect, url_for


@home.route('/login/')
def login():
    return render_template('home/login.html')

@home.route('/logout/')
def logout():
    return redirect(url_for('home.login'))

@home.route('/regist/')
def regist():
    return render_template('home/regist.html')

@home.route('/user/')
def user():
    return render_template('home/user.html')

@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')

@home.route('/comments/')
def comments():
    return render_template('home/comments.html')

@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')

@home.route('/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/animation/')
def animation():
    return render_template('home/animation.html')

@home.route('/search/')
def search():
    return render_template('home/search.html')

@home.route('/play/')
def play():
    return render_template('home/play.html')

# 配置404页面,需要在蓝图初始化的时候定义
# @home.errorhandler(404)
# def page_not_found(error):
#     return render_template('home/404.html'), 404
