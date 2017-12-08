# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:18
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/movie?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 会员表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.TEXT)
    face = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    uuid = db.Column(db.String(255), unique=True)


    user_logs = db.relationship('Userlog', backref='user') # 会员日志外键关系关联
    comments = db.relationship('Comment', backref='user') # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name

# 会员登录日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Userlog %r>' % self.id


# 标签
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    movies = db.relationship('Movie', backref='tag') # 电影的外键关联

    def __repr__(self):
        return '<Tag %r>' % self.name

# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    play_num = db.Column(db.BigInteger)
    comment_num = db.Column(db.BigInteger)
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    comments = db.relationship('Comment', backref='movie')  # 关联用户的评论
    moviecols = db.relationship('Moviecol', backref='movie')  # 关联用户的评论

    def __repr__(self):
        return '<Movie %r>' % self.title

# 上映预告
class Preview(db.Model):
    __tablename__ = 'preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Preview %r>' % self.title


# 评论
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % self.id

# 电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Moviecol %r>' % self.id

# 权限
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Auth %r>' % self.name

# 角色
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    admin = db.relationship('Admin', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

# 管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)
    is_super = db.Column(db.SmallInteger) # 0为超级管理员
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 角色
    admin_log = db.relationship('Adminlog', backref='admin')
    oplog = db.relationship('Oplog', backref='admin')

    def __repr__(self):
        return '<Admin %r>' % self.id


# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):
        return '<Adminlog %r>' % self.id

# 操作日志
class Oplog(db.Model):
    __tablename__ = 'oplog'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):
        return '<Oplog %r>' % self.id

if __name__ == '__main__':
     db.create_all()
    # role = Role(name='hello', auths='')
    # db.session.add(role)
    # db.session.commit()
























