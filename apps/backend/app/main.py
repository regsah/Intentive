from fastapi import FastAPI, HTTPException
from app.api.routes import router

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"Hello": "World"}