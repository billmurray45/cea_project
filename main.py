import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.users.routes import router as users_router

app = FastAPI(
    title="CEA YU Project",
    description="SSR Landing website for Yessenov University's CEA Project",
    version="1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(users_router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """ Главная Landing страница """
    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
