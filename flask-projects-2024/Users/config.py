import os

# 配置類
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # 密鑰
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'  # 資料庫 URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用資料庫修改追蹤