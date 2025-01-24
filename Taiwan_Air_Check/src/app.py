import os
import requests
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

DATA_URL = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=JSON'

@app.route('/')
def home():
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        data = response.json()['records']
        df = pd.DataFrame(data).head(20)  # 簡化只顯示前 20 筆
        return render_template('index.html', records=df.to_dict(orient='records'))  # 渲染模板並傳遞數據
    else:
        return f"無法取得資料，錯誤代碼: {response.status_code}", 500

@app.route('/data')
def data():
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        data = response.json()['records']
        return jsonify(data[:20])  # 返回前 20 筆數據
    else:
        return jsonify({"error": "無法取得資料"}), 500

if __name__ == '__main__':
    app.run(debug=True)