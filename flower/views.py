from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Image as ImageModel  # PillowのImageと区別するために変更
from .recognition.recognize import main
from PIL import Image  # PillowのImageをインポート
import os

def showall(request):
    images = ImageModel.objects.all().order_by("-pk")
    context = {"images": images}
    return render(request, "flower/showall.html", context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # データベースに画像を保存
            form.save()

            # 最新の画像を取得
            img = ImageModel.objects.get(pk=ImageModel.objects.count())
            
            # 画像のパスを取得してPillowで開く
            img_path = img.picture.path  # Djangoモデルの画像パス
            pil_img = Image.open(img_path)  # Pillowで画像を開く

            # 画像を572x500ピクセルにリサイズ
            pil_img = pil_img.resize((572, 500), Image.LANCZOS)

            # リサイズ後の画像を同じ場所に保存
            pil_img.save(img_path)

            # 推論結果を取得して、モデルに保存
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
            
            # フォームデータの保存
            img.save()

            # 結果ページにリダイレクト
            return redirect("flower:result")
    else:
        form = ImageForm()

    context = {"form": form}
    return render(request, "flower/upload.html", context)

def result(request):
    images = ImageModel.objects.all().order_by("-pk")
    context = {"images": images[1:], "now_image": images[0]}
    return render(request, "flower/result.html", context)
