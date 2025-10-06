from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["users"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        "users/register.html",
        {
            "request": request
        }
    )


@router.post("/register", response_class=HTMLResponse)
async def register(
        request: Request,
        session: AsyncSession,
        email: str = Form(...),
        username: str = Form(...),
        password: str = Form(...),
        full_name: str = Form(None),
):
    pass
