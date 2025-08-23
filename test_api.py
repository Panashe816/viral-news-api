# test_api.py
from fastapi import FastAPI
from database import engine
import models

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Test successful!", "status": "working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)