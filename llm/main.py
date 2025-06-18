from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

LLAMA_SERVER_URL = "http://192.168.123.105:8000/completion"  

class PromptRequest(BaseModel):
    prompt: str
    n_predict: int = 128

@app.post("/llama")
async def llama_inference(request: PromptRequest):
    try:
        payload = {
            "prompt": request.prompt,
            "n_predict": request.n_predict
        }
        response = requests.post(LLAMA_SERVER_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
