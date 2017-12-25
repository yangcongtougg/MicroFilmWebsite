# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Admin


class LoginForm(FlaskForm):
    """管理员登录表单, StringFiled, PasswordField, SubmitField 用来生成html中标签的属性"""
    account = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号')
        ],  # 验证器,不能为空
        description='账号',
        render_kw={'class': 'form-control', 'placeholder': '请输入账号'}
    )
    pwd = PasswordField(
        label='密码',
        validators=[DataRequired('请输入密码')],
        description='密码',
        render_kw={'class': 'form-control', 'placeholder': '请输入密码'}
    )
    submit = SubmitField(
        '登录',
        render_kw={'class': 'btn btn-primary btn-block btn-flat'}
    )

    def validate_account(self, filed):  # 查询数据库，admin表下面有没有这个账号
        account = filed.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('账号不存在')


class TagForm(FlaskForm):
    '''
    这里的name和submit代替了html form表单里的标签,这里的东西定义之后相应的html里的标签就可以删除了
    '''
    name = StringField(label='名称', validators=[DataRequired('请输入标签!')], description='标签', render_kw={
        'class': 'form-control', 'id': 'input_name', 'placeholder': '请输入标签名称!'
    })
    submit = SubmitField('添加', render_kw={'class': 'btn btn-primary'})
