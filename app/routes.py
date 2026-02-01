from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

TOTAL_GAMES = 9

def require_game(request: Request, game_num: int):
    current = request.session.get("current_game", 0)
    return current == game_num

@router.get("/")
def home(request: Request):
    request.session.clear()
    request.session["current_game"] = 1
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/game/{num}")
def game(request: Request, num: int):
    if not require_game(request, num):
        return RedirectResponse(f"/game/{request.session.get('current_game',1)}", status_code=302)
    return templates.TemplateResponse(f"game{num}.html", {"request": request})

@router.post("/complete/{num}")
def complete(request: Request, num: int):
    if require_game(request, num):
        request.session["current_game"] += 1
    return RedirectResponse(f"/game/{request.session['current_game']}", status_code=302)
