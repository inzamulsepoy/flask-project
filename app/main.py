from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status

from .database import SessionLocal, engine
from .models import User, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    success = request.query_params.get("success")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "success": success}
    )


@app.post("/submit")
def submit_form(
    name: str = Form(...),
    email: str = Form(...)
):
    db = SessionLocal()

    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.close()

    return RedirectResponse(
        url="/?success=1",
        status_code=status.HTTP_303_SEE_OTHER
    )
