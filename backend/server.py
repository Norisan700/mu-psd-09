from flask import Flask, request , jsonify
from flask_cors import CORS
from PIL import Image
import joblib
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

# URL「/」に対応して処理する関数
@app.route("/main")
def index():
    # 戻り値がそのままWebサイトに表示される。
    return jsonify({"result":"This is MY Backend API Server."})
@app.route("/help")
def help():
    return "This is Help Page!!"


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['image']
    
    # 画像を開く
    try:
        image = Image.open(file.stream)
        # 画像処理があればここで行う

        return jsonify({"message": "Image received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# サーバ起動用の設定
if __name__ == "__main__":
    app.run(debug=True)

