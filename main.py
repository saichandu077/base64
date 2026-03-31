
from fastapi import FastAPI, UploadFile, File
import base64
from mangum import Mangum

app = FastAPI()

@app.post("/encode-image")
async def encode_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    encoded_string = base64.b64encode(image_bytes).decode("ascii")
    return {"filename": file.filename, "base64": encoded_string}

handler = Mangum(app)
