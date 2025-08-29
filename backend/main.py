from fastapi import FastAPI
from routers.drug_info import router as drug_info_router
import uvicorn


app = FastAPI()

app.include_router(drug_info_router, prefix="/drug_info")


@app.get("/")
def home():
    return {"Message": "Welcome to Medify"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
