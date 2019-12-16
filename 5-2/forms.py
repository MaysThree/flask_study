from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class BaseLogin(Form):
    name = StringField('name',
                       validators=[DataRequired(message='用户名不能为空'),
                                   Length(6, 16, message='长度位于6-16')],
                       render_kw={'placeholder': '输入用户名'})
    password = PasswordField('password',
                             validators=[DataRequired(message='密码不能为空'),
                                         Length(6, 16, message='长度位于6-16')],
                             render_kw={'placeholder': '输入密码'})
