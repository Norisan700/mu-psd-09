from flask import Flask, request , jsonify
from flask_cors import CORS
from PIL import Image
import joblib
import pandas as pd
import io
import os

from django.shortcuts import redirect, render
from forms import ImageForm

# Create your views here.
from .models import Image
from .recognize import main

def showall(request):
    images = Image.objects.all().order_by("-pk")
    context = {"images": images}
    return render(request, "flower/showall.html", context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Image.objects.get(pk=Image.objects.count())
            output = main(img.picture)
            img.first_name = output[0][0]
            img.first_value = output[0][1]
            img.second_name = output[1][0]
            img.second_value = output[1][1]
            img.third_name = output[2][0]
            img.third_value = output[2][1]
            img.fourth_name = output[3][0]
            img.fourth_value = output[3][1]
            img.fifth_name = output[4][0]
            img.fifth_value = output[4][1]
            img.save()
            return redirect("flower:result")
    else:
        form = ImageForm()
    context = {"form": form}
    return render(request, "flower/upload.html", context)

def result(request):
    images = Image.objects.all().order_by("-pk")
    context = {"images": images[1:], "now_image": images[0]}
    return render(request, "flower/result.html", context)

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
        # 画像処理
        model = joblib.load('\save_model\model_20.pth')
        ret = model.predict('image')

        return jsonify({"message": "Image received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# サーバ起動用の設定
if __name__ == "__main__":
    app.run(debug=True)

