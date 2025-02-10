# Flask Recipe

這是一個基於 Flask 的食譜管理系統，提供用戶註冊、登入、登出、查看和管理食譜等功能。

## 功能

- 用戶註冊與登入
- 查看與管理個人資料
- 忘記密碼與重設密碼
- 新增、編輯與刪除食譜
- 查看所有食譜與單個食譜詳情
- 管理者頁面

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Recipe
    ```

2. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```

3. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```

4. 設定環境變數：
    建立 `.env` 文件並設定必要的環境變數，例如資料庫連接字串、郵件伺服器設定等。

5. 初始化資料庫：
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. 啟動伺服器：
    ```bash
    flask run
    ```

## 使用說明

### 註冊新帳號
1. 訪問 `/register` 頁面。
2. 填寫註冊表單並提交。

### 登入
1. 訪問 `/login` 頁面。
2. 填寫登入表單並提交。

### 登出
1. 訪問 `/logout` 頁面以登出。

### 查看與管理個人資料
1. 登入後訪問 `/profile` 頁面查看與編輯個人資料。

### 忘記密碼
1. 訪問 `/forgot-password` 頁面，輸入電子郵件以接收重設密碼連結。

### 新增食譜
1. 登入後訪問 `/recipe/create` 頁面，填寫表單並提交以新增食譜。

### 編輯食譜
1. 登入後訪問 `/recipe/<int:recipe_id>` 頁面，填寫表單並提交以編輯食譜。

### 刪除食譜
1. 登入後訪問 `/recipe/<int:recipe_id>` 頁面，點擊刪除按鈕以刪除食譜。

## 測試
使用 pytest 進行測試：
```bash
pytest
```

# 觀看Demo
[Demo 影片](https://youtu.be/q6tD8qz2ZwA)