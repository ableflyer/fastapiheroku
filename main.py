import fastapi as fpi
from OCRTest import ocr

app = fpi.FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, it works"}
@app.get("/image/{url}")
def urlscan(url: str):
    return {"Text": ocr(url)}
