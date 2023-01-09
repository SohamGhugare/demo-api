from fastapi import FastAPI
from uvicorn import run
from os import getenv

app = FastAPI()

@app.get("/")
async def index():
    return {"data": "root"}

@app.get("/{inp}")
async def get_input(inp: str):
    print({"input_data": inp})


if __name__ == "__main__":
    # run("api:app", reload=True)
    run("api:app", host="0.0.0.0", port=getenv("PORT", default=5000), log_level="info")