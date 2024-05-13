from cs1media import *
from PIL import Image

white = (255, 255, 255)
black = (0, 0, 0)

# hide bwimg into img
def hide_picture(img, bwimg):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1: 
                r = r - 1
            img.set(x, y, (r, g, b))
    w1, h1 = bwimg.size()
    for y in range(h1):
        for x in range(w1):
            r, g, b = img.get(x, y)
            if bwimg.get(x, y) == black:
                r = r + 1
            img.set(x, y, (r, g, b))

def restore_picture(img):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1: 
                img.set(x, y, black)
            else: 
                img.set(x, y, white)

statue = load_picture("./photos/statue2.jpg")
yuna = load_picture("./photos/BWyuna1.jpg")
hide_picture(statue, yuna)
statue.show()
restore_picture(statue)
statue.show()

# 이미지 파일 경로
# output_file_path = ""
# 이미지 저장
# 이미지를 jpg 파일로 저장하는 함수
# def save_as_jpg(picture, file_path):
#     # 품질을 100으로 설정하여 최대 품질로 저장
#     picture.save_as(file_path)
# save_as_jpg(statue, output_file_path)