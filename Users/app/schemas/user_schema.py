from marshmallow import Schema, fields

# 定義 User 的序列化 Schema
class UserSchema(Schema):
    username = fields.Str(required=True)  # 必填的使用者名稱欄位
    email = fields.Email(required=True)  # 必填的電子郵件欄位
    password = fields.Str(required=True)  # 必填的密碼欄位
    phone = fields.Str()  # 電話號碼欄位
    bio = fields.Str()  # 簡介欄位
    address = fields.Str()  # 地址欄位
    is_owner = fields.Boolean()  # 老闆身分欄位
    created_at = fields.DateTime(dump_only=True)  # 只讀建立時間欄位