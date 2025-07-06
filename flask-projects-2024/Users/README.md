# Flask Users

## 專案簡介
這是一個使用 Flask 框架開發的用戶管理系統，包含註冊、登入、登出、編輯個人資料等功能。

## 功能介紹
- 註冊新帳號
- 使用者登入/登出
- 編輯個人資料
- 查看個人資料
- 老闆與客人儀表板

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Users
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

### 查看個人資料
1. 登入後訪問 `/profile/<user_id>` 頁面查看個人資料。

### 編輯個人資料
1. 登入後訪問 `/edit_profile` 頁面。
2. 填寫並提交編輯表單。

