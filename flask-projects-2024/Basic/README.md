# Flask Basic

這是一個基於 Flask 的基本應用程式，提供用戶註冊、登入、登出、查看和管理個人資料等功能。

## 功能

- 用戶註冊與登入
- 查看與管理個人資料
- 忘記密碼與重設密碼
- 管理員頁面

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Basic
    ```

2. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```

3. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```

4. 建立資料庫：
    ```bash
    flask init-db
    ```

5. 啟動 Flask 應用程式：
    ```bash
    flask run
    ```

## 使用說明

1. 在瀏覽器中訪問 `http://127.0.0.1:5000`。
2. 註冊新帳號並登入。
3. 查看與管理個人資料。
4. 忘記密碼時可重設密碼。
5. 管理員可訪問管理員頁面進行用戶管理。

## 測試

1. 運行測試：
    ```bash
    pytest
    ```