# Flask Stock Prediction

這是一個基於 Flask 的股市預測系統，使用 `yfinance` 獲取股票數據，並使用 `scikit-learn` 進行線性回歸預測未來的股票價格。該系統可以顯示過去三個月的股票數據、當前價格以及預測未來一個月的價格。

## 功能

- 獲取過去三個月的股票數據
- 顯示股票數據圖表
- 顯示當前價格
- 預測未來一個月的價格

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Stock-Prediction
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

1. 啟動 Flask 伺服器：
    ```bash
    flask run
    ```

2. 在瀏覽器中訪問 `http://127.0.0.1:5000`。

3. 輸入股票代號（例如：AAPL）並點擊「預測」按鈕。

## 範例

- 輸入 `AAPL` 並點擊「預測」按鈕，系統將顯示 Apple Inc. 的過去三個月的股票數據圖表、當前價格以及預測未來一個月的價格。

## 觀看 Demo
[Demo 影片](https://youtu.be/sKQV2DIWqgo)