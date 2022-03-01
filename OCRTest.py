import easyocr
# image_path = 'pycode.png'
# reader = easyocr.Reader(['en'], gpu=False)
# result = reader.readtext(image_path)
# for i in result:
#     print(i[1])
import pytesseract as pyt
import urllib.request
import numpy as np
import cv2
from PIL import Image


def ocr(url):
    urllib.request.urlretrieve(url, "test.png")
    cv2.imread("test.png")
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    c = pyt.image_to_string(Image.open("test.png"))
    return c
