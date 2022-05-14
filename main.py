import fastapi as fpi
import pytesseract as pyt
import urllib.request
import numpy as np
import cv2
from PIL import Image
import sys, os
from starlette.requests import Request
import io
import requests
from pydantic import BaseModel

app = fpi.FastAPI()


# @app.post("/predict/")
# def prediction(request: Request,
#                file: bytes = fpi.File(...)):
#     if request.method == "POST":
#         img = ImageType()
#         img.
#         image_stream = io.BytesIO(file)
#         image_stream.seek(0)
#         file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
#         # urllib.request.urlretrieve(url, "test.png")
#         # cv2.imread("test.png")
#         pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#         frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         c = pyt.image_to_string(frame)
#         return c
#     return "No label found"
@app.get("/")
def text():
    return {"text", "Hello"}


