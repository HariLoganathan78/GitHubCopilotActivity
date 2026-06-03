from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Welcome to the webpage, Hari Loganathan!"
    }

@app.post("/checksum")
def checksum(data: TextRequest):
    checksum_value = hashlib.md5(data.text.encode()).hexdigest()

    return {
        "text": data.text,
        "checksum": checksum_value
    }
