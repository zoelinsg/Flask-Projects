from app import create_app

# 創建 Flask 應用實例
app = create_app()

# 運行應用
if __name__ == "__main__":
    app.run()