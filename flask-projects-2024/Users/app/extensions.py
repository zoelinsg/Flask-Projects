from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 初始化 SQLAlchemy
db = SQLAlchemy()

# 初始化 Migrate
migrate = Migrate()