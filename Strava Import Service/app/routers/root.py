from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse("root.html", context={"request": request})



