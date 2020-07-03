from PIL import Image
import os
import math

def aspect_calcurator(height, width):
    cal_number = width
    rest = height % cal_number
    while rest > 0:
        now_rest = cal_number % rest
        cal_number = rest
        rest = now_rest
    height_aspect = math.trunc(height / cal_number)
    width_aspect = math.trunc(width / cal_number)
    msg = "縦" + str(height) + "px 横" + str(width) + "px アスペクト比" + str(width_aspect) + ":" + str(height_aspect) + "です"
    return msg

print("画像ファイルのパスを入力してください")
path=str(input())
height = Image.open(path).height
width = Image.open(path).width
print(aspect_calcurator(height, width))
print("この画像のサイズは"+str(os.path.getsize(path))+"バイトです")