# Flask Taiwan AQI Top 20

這是一個使用 Flask 框架構建的網頁應用程式，用於顯示臺灣各地的空氣品質指標（AQI）前 20 名的數據。數據來源於臺灣環保署的公開 API。

## 功能

- 從臺灣環保署 API 獲取 AQI 數據
- 顯示前 20 名的 AQI 數據
- 以表格形式展示數據

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Taiwan_Air_Check
    ```

2. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```

3. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```

4. 啟動伺服器：
    ```bash
    flask run
    ```

## 使用說明

### 瀏覽首頁
1. 訪問 `/` 頁面以查看前 20 名的 AQI 數據。

### 獲取數據 API
1. 訪問 `/data` 頁面以獲取前 20 名的 AQI 數據（JSON 格式）。

## 觀看 Demo
[Demo 影片](https://youtu.be/nOe2NlTo9lM)