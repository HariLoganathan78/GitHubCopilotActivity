from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI(
    title="Containerized Python API",
    description="API for generating checksums from text",
    version="1.0"
)

# Model for accepting JSON input
class TextRequest(BaseModel):
    text: str

# Welcome page
@app.get("/")
def home():
    return {
        "message": "Welcome to the webpage, Hari Loganathan!"
    }

# Generate checksum from text
@app.post("/checksum")
def checksum(data: TextRequest):
    checksum_value = hashlib.md5(data.text.encode()).hexdigest()

    return {
        "text": data.text,
        "checksum": checksum_value
    }
