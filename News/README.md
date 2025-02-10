# Flask News

這是一個使用 Flask、Bootstrap、Sass 和 NewsAPI 建立的世界新聞網頁，能夠抓取 API 資料以獲取最新的世界新聞。

## 參考教程
[Flask News Tutorial](https://www.youtube.com/watch?v=5EUOvXjahLY&t=21s)

## 功能

- 獲取最新世界新聞
- 使用關鍵字搜尋新聞
- 過濾特定來源和標題的新聞

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd News
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
    在 config.py 並設定必要的環境變數，例如 News API 金鑰。

5. 啟動伺服器：
    ```bash
    flask run
    ```

## 使用說明

1. 使用搜尋框輸入關鍵字以搜尋新聞。
2. 使用分類篩選相關新聞。
3. 點選首頁查看所有最新新聞。

## 查看 Demo
[Demo 影片](https://youtu.be/9r1nao88deY)