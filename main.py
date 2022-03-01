import fastapi as fpi
from OCRTest import ocr

app = fpi.FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, it works"}


@app.get("/image/{url}")
def urlscan(url: str):
    text = ocr(url)
    return {"Text": url}
