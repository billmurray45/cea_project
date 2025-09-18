import uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="CEA YU Project",
    description="SSR Landing website for Yessenov University's CEA Project",
    version="1.0",
)


@app.get("/")
async def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
