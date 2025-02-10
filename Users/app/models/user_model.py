import bcrypt
from ..extensions import db

# 定義 User 模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主鍵 ID
    username = db.Column(db.String(150), nullable=False, unique=True)  # 使用者名稱
    email = db.Column(db.String(150), nullable=False, unique=True)  # 電子郵件
    password_hash = db.Column(db.String(200), nullable=False)  # 雜湊密碼
    is_owner = db.Column(db.Boolean, nullable=False, default=False)  # 分老闆和客人身分，老闆 (True/False)
    phone = db.Column(db.String(20), nullable=True)  # 電話號碼
    bio = db.Column(db.String(150), nullable=True)  # 簡介
    address = db.Column(db.String(150), nullable=True)  # 地址

    def set_password(self, password):
        """
        設定密碼（雜湊處理）
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """
        驗證密碼
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        定義物件的字串表示形式
        """
        return f'<User {self.username}>'