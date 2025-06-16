from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Hello World", tags=["Hello World"])
async def root():
    return {"message": "Hello World"}