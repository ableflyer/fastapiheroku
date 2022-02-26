import fastapi as fpi

app = fpi.FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, it works"}
