# main.py
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cloud Run is working!"}

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)



@app.get("/hello")
def name_check():
    return JSONResponse(content={"name": "Hello Sarang Bro"}, status_code=200)

