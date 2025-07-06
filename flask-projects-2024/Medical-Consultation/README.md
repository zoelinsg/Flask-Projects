# Flask Medical Consultation

這是一個基於 Flask 的簡單醫療問診系統，允許用戶提交症狀並獲得診斷結果。

## 功能

- 提交症狀表單
- 根據症狀進行診斷
- 顯示診斷結果

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地：
    ```sh
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Medical-Consultation
    ```

2. 安裝依賴：
    ```sh
    poetry install
    ```

3. 進入虛擬環境：
    ```sh
    poetry shell
    ```

4. 建立資料庫：
    ```sh
    python
    ```
    在 Python 互動式環境中，執行以下代碼來建立資料庫：
    ```python
    from src.models import Base
    from src.utils.database import engine

    Base.metadata.create_all(engine)
    ```
    然後退出 Python 互動式環境：
    ```python
    exit()
    ```

5. 啟動 Flask 應用：
    ```sh
    flask run
    ```

## 使用說明

1. 在瀏覽器中訪問 `http://127.0.0.1:5000`。
2. 輸入症狀並提交以獲取診斷結果。

## 測試

1. 運行測試：
    ```sh
    pytest
    ```

## 觀看 Demo
[Demo 影片](https://youtu.be/S9_qr19datE)