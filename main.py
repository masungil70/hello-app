from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

# 정적 파일 경로 (이미지 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_photos(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })
