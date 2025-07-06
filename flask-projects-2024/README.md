# Flask-Projects
包含多個基於 Flask 的 RESTful API 專案集合。

## 專案列表
- **Basic**：用戶註冊、登入、登出、查看和管理個人資料等。
- **Chat**：即時聊天應用程式，允許用戶創建或加入聊天室並進行即時聊天。
- **NFT Image Generator**：上傳圖片並生成對應的 NFT metadata。
- **Medical Consultation**：提交症狀並獲得診斷結果。
- **Music Recommendation**：根據用戶輸入的音樂類型推薦音樂。
- **News**：顯示最新的世界新聞，使用 NewsAPI 獲取新聞數據。
- **Posts**：博客系統，提供用戶註冊、登入、發表帖子、評論和點讚等功能。
- **Recipe**：食譜管理系統，提供用戶註冊、登入、查看和管理食譜等功能。
- **Stock Prediction**：獲取股票數據並進行預測。
- **Taiwan Air AQI**：顯示臺灣各地的空氣品質指標（AQI）。
- **Users**：用戶管理系統，包含註冊、登入、登出、編輯個人資料、登入不同儀表板等功能。

## 安裝與設定
### 環境設定
- Python 3.12 或以上版本
- Poetry

### 安裝步驟
1. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Flask-Projects.git
    ```
2. 進入各個專案目錄，使用 Poetry 安裝依賴：
    ```bash
    cd <project-directory>
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
