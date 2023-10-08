
import uvicorn
from ultralytics import YOLO
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ultralytics.utils.ops import scale_image
from collections import Counter

from io import BytesIO

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
model = YOLO('static/models/yolov8n-seg.pt')

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.post("/vehicle_segment")
#async def image_detect(request: Request):
async def image_detect(file: UploadFile):
    print(file.filename)
    return FileResponse(file.file)
    #img = cv2.imread("dogs.jpg")
    #result = model.predict(img, save=False)
    #json_result = result.tojson()
    #result = await request.body()
    #print(result)
    #return result
    # return await JSONResponse(
    #             {
    #                 #"image": result,
    #             },
    #             status_code=200,
    #         )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)