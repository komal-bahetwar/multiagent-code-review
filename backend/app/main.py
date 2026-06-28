from fastapi import FastAPI

app = FastAPI(title="Multi-Agent Code Review API")


@app.get("/")
def health():
    return {"status": "running"}