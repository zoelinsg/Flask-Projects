from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# 定義 User 表單
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # 使用者名稱
    email = StringField('Email', validators=[DataRequired()])  # 電子郵件
    password = StringField('Password', validators=[DataRequired()])  # 密碼
    phone = StringField('Phone')  # 電話號碼
    bio = StringField('Bio')  # 簡介
    address = StringField('Address')  # 地址
    is_owner = BooleanField('Is Owner')  # 老闆身分