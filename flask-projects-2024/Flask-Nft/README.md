# NFT Image Generator

這是一個使用 Flask 構建的簡單應用程式，用於上傳圖片並生成對應的 NFT metadata。

## 功能說明

- 上傳圖片文件
- 生成圖片的 NFT metadata，包括名稱、格式、尺寸和唯一的 Token ID
- 將生成的 metadata 顯示在網頁上

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Flask-Nft
    ```

2. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```

3. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```

4. 啟動 Flask 應用程式：
    ```bash
    flask run
    ```

## 使用說明

1. 在瀏覽器中訪問 `http://127.0.0.1:5000`。
2. 上傳圖片文件並生成對應的 NFT metadata。

