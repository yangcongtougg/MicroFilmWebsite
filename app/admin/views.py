# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from app.admin import admin
from flask import render_template, redirect, url_for


@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/login/')
def login():
    return render_template('admin/login.html')

@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))

@admin.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')

@admin.route('/tag/add/')
def tag_add():
    return render_template('admin/tag_add.html')

@admin.route('/tag/list/')
def tag_list():
    return render_template('admin/tag_list.html')

# @admin.route('/')
# def index():
#     return render_template('admin/index.html')
#
# @admin.route('/')
# def index():
#     return render_template('admin/index.html')
#
# @admin.route('/')
# def index():
#     return render_template('admin/index.html')
#
# @admin.route('/')
# def index():
#     return render_template('admin/index.html')
#
# @admin.route('/')
# def index():
#     return render_template('admin/index.html')
