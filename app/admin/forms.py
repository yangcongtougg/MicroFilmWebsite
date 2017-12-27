# _*_ coding: utf-8 _*_
# @Time     :2017/12/5 11:20
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError

from app.models import Admin, Tag

tags = Tag.query.all()


# log提交表单
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


# 标签表单
class TagForm(FlaskForm):
    '''
    这里的name和submit代替了html form表单里的标签,这里的东西定义之后相应的html里的标签就可以删除了
    '''
    name = StringField(label='名称', validators=[DataRequired('请输入标签!')], description='标签', render_kw={
        'class': 'form-control', 'id': 'input_name', 'placeholder': '请输入标签名称!'
    })
    submit = SubmitField('编辑', render_kw={'class': 'btn btn-primary'})


# 电影表单
class MovieForm(FlaskForm):
    title = StringField(label='片名', validators=[DataRequired('请输入片名!')], description='片名', render_kw={
        'class': 'form-control', 'id': 'input_title', 'placeholder': '请输入片名!'
    })

    url = FileField(label='文件', validators=[DataRequired('请上传电影文件')], description='文件')

    info = TextAreaField(label='简介', validators=[DataRequired('请输入电影简介')], description='简介', render_kw={
        'class': 'form-control', 'rows': 10
    })

    logo = FileField(label='封面', validators=[DataRequired('请上传电影封面')], description='封面')

    star = SelectField(label='星级', validators=[DataRequired('请选择星级')], coerce=int, choices=[
        (1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')], render_kw={
        'class': 'form-control'
    })

    tag_id = SelectField(label='标签', validators=[DataRequired('请选择标签')], coerce=int,
                         choices=[(i.id, i.name) for i in tags], render_kw={
            'class': 'form-control'
        })

    area = StringField(label='地区', validators=[DataRequired('请输入地区!')], description='地区', render_kw={
        'class': 'form-control', 'placeholder': '请输入电影地区!'
    })

    length = StringField(label='片长', validators=[DataRequired('请输入片长!')], description='片长', render_kw={
        'class': 'form-control', 'placeholder': '请输入片长!'
    })

    release_time = StringField(label='上映时间', validators=[DataRequired('请输入上映时间!')], description='上映时间', render_kw={
        'class': 'form-control', 'id': 'input_release_time', 'placeholder': '请输入上映时间!'
    })

    submit = SubmitField('添加', render_kw={'class': 'btn btn-primary'})


class PreviewForm(FlaskForm):
    title = StringField(
        label='预告标题',
        validators=[DataRequired('请输入预告标题!')],
        description='预告标题',
        render_kw={'class': 'form-control', 'id': 'input_title', 'placeholder': '请输入预告标题!'}
    )
    logo = FileField(
        label='预告封面',
        validators=[DataRequired('请上传预告封面')],
        description='电影预告封面'
    )

    submit = SubmitField('添加', render_kw={'class': 'btn btn-primary'})
