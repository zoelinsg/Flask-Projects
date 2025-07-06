# Flask Music Recommendation

這是一個基於 Flask 的音樂推薦系統，使用 Spotify API 根據用戶輸入的音樂類型推薦音樂。

## 功能

- 根據音樂類型推薦音樂
- 顯示推薦的音樂列表，包括曲名、藝術家和播放鏈接

## 安裝與設定

### 先決條件
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    cd Music-Recommendation
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
    建立 `.env` 文件並設定以下環境變數：
    ```plaintext
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    ```

5. 啟動伺服器：
    ```bash
    flask run
    ```

## 使用說明

1. 輸入音樂類型並點擊「推薦」按鈕以獲取音樂推薦列表。


## 觀看Demo
[Demo 影片](https://youtu.be/UXFB2k75z-U)