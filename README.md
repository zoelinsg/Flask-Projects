# Flask-Projects

包含多個基於 Flask 的 RESTful API 專案集合。

## 專案列表

1. **Basic**
    - 功能：用戶註冊、登入、登出、查看和管理個人資料等。

2. **Chat**
    - 功能：即時聊天應用程式，允許用戶創建或加入聊天室並進行即時聊天。

3. **NFT Image Generator**
    - 功能：上傳圖片並生成對應的 NFT metadata。

4. **Medical Consultation**
    - 功能：提交症狀並獲得診斷結果。

5. **Music Recommendation**
    - 功能：根據用戶輸入的音樂類型推薦音樂。

6. **News**
    - 功能：顯示最新的世界新聞，使用 NewsAPI 獲取新聞數據。

7. **Posts**
    - 功能：博客系統，提供用戶註冊、登入、發表帖子、評論和點讚等功能。

8. **Recipe**
    - 功能：食譜管理系統，提供用戶註冊、登入、查看和管理食譜等功能。

9. **Stock Prediction**
    - 功能：獲取股票數據並進行預測。

10. **Taiwan Air AQI**
    - 功能：顯示臺灣各地的空氣品質指標（AQI）。

11. **Users**
    - 功能：用戶管理系統，包含註冊、登入、登出、編輯個人資料、登入不同儀表板等功能。

## 安裝與設定

### 先決條件
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
