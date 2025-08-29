from fastapi import FastAPI
from routers.drug_info import router as drug_info_router
from routers.ai_router import router as ai_router
import uvicorn


app = FastAPI()

app.include_router(drug_info_router, prefix="/drug_info", tags=["Drug Information"])
app.include_router(ai_router, prefix="/ai", tags=["AI Services"])


@app.get("/")
def home():
    return {"Message": "Welcome to Medify. Use /docs for API documentation."}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
