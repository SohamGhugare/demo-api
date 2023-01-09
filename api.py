from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/")
async def index():
    return {"data": "root"}

@app.get("/{inp}")
async def get_input(inp: str):
    print({"input_data": inp})


if __name__ == "__main__":
    run("api:app", reload=True)