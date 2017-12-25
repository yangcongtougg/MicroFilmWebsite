# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from flask import render_template, redirect, url_for, flash, session, request

from app.admin import admin
from app.admin.forms import LoginForm, TagForm
from app.models import Admin, Tag
from functools import wraps
from app import db

# 访问控制器必须登录,相当于路由的拦截器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function



@admin.route('/')
@admin_login_req
def index():
    return render_template('admin/index.html')


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # 表示提交的时候要进行验证
        data = form.data # 表单的数据根据form.data来获取
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误!')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account'] # 如果账号是正确的我们就要定义一个session的会话来保存我们的账号
        return redirect(url_for('admin.index') or request.args.get('next'))
    return render_template('admin/login.html', form=form)


@admin.route('/logout/')
@admin_login_req
def logout():
    session.pop('account', None)
    return redirect(url_for('admin.login'))


@admin.route('/pwd/')
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')


@admin.route('/tag/add/', methods=['GET', 'POST'])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data['name']).count()
        if tag == 1:
            flash('名称已经存在，不能重复添加', 'err')
            return redirect(url_for('admin.tag_add'))
        tag = Tag(name=data['name'])
        db.session.add(tag)
        db.session.commit()
        flash('标签添加成功', 'ok')
        return redirect(url_for('admin.tag_add'))
    return render_template('admin/tag_add.html', form=form)


@admin.route('/tag/list/')
@admin_login_req
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/movie/add/')
@admin_login_req
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie/list/')
@admin_login_req
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/preview/add/')
@admin_login_req
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/preview/list/')
@admin_login_req
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/user/list/')
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/user/view/')
@admin_login_req
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/comment/list/')
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/moviecol/list/')
@admin_login_req
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/oplog/list/')
@admin_login_req
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route('/adminloginlog/list/')
@admin_login_req
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/userloginlog/list/')
@admin_login_req
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/auth/add/')
@admin_login_req
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth/list/')
@admin_login_req
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/role/add/')
@admin_login_req
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role/list/')
@admin_login_req
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/admin/add/')
@admin_login_req
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin/list/')
@admin_login_req
def admin_list():
    return render_template('admin/admin_list.html')
