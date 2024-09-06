from flask import Flask,jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# URL「/」に対応して処理する関数
@app.route("/help")
#def index():
    # 戻り値がそのままWebサイトに表示される。
#    return jsonify({"result":"This is MY Backend API Server."})
def help():
    return "This is Help Page!!"


# データ検索用関数
# URLルーティングの<income>,<rooms>,<ages>がそれぞれ関数の引数に入ってくる。
@app.route("/calc/<income>/<rooms>/<ages>")
def calculate(income,rooms,ages):
    # 引数の作成
    data={"MedInc":[income],"HouseAge":[ages],"AveRooms":[rooms]}
    param=pd.DataFrame(data)

    # AIモデルの読込
    model = joblib.load('model.pkl')

    # 先読み実行
    ret=y_pred=model.predict(param)

    # 得られた結果をJSON形式にして返す
    price=ret[0]
    return jsonify({"price":price})


# サーバ起動用の設定
if __name__ == "__main__":
    app.run(debug=True)

