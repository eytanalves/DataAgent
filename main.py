import os.path
from fastapi import FastAPI, HTTPException, UploadFile, Form, File
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
from data_ai.data_processor import AIAgent
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles


class AskModel(BaseModel):
    question: str

app = FastAPI()
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

ai_agent = AIAgent()


@app.get("/")
async def read_main():
    with open(os.path.join('templates/home.html'), 'r') as f:
        content = f.read()
    return HTMLResponse(content=content)


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...), sheet_name: str = Form(None)):
    return await ai_agent.upload_files(files, sheet_name)


@app.post("/ask", response_class=JSONResponse)
async def ask_ai(ask: AskModel):
    if ai_agent is None:
        raise HTTPException(status_code=400, detail="No data uploaded yet. Please upload data first.")
    response = ai_agent.run_agent(ask.question)
    return JSONResponse(content={"response": response})
