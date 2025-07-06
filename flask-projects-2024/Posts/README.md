# Flask Posts

這是一個基於 Flask 的博客系統，提供用戶註冊、登入、發表帖子、評論和點讚等功能。

## 參考教程
[Flask Blog Tutorial](https://github.com/techwithtim/Flask-Blog-Tutorial)

## 功能

- 用戶註冊與登入
- 發表新帖子
- 查看所有帖子
- 刪除帖子
- 發表評論
- 刪除評論
- 點讚與取消點讚

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Posts
    ```

2. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```

3. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```

4. 初始化資料庫：
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. 啟動伺服器：
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

### 發表新帖子
1. 登入後訪問 `/create-post` 頁面。
2. 填寫表單並提交以發表新帖子。

### 查看所有帖子
1. 登入後訪問 `/` 或 `/home` 頁面查看所有帖子。

### 刪除帖子
1. 登入後訪問 `/delete-post/<id>` 頁面以刪除帖子。

### 發表評論
1. 登入後訪問 `/create-comment/<post_id>` 頁面，填寫表單並提交以發表評論。

### 刪除評論
1. 登入後訪問 `/delete-comment/<comment_id>` 頁面以刪除評論。

### 點讚與取消點讚
1. 登入後訪問 `/like-post/<post_id>` 頁面以點讚或取消點讚。
