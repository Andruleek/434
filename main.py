from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return HTMLResponse(templates.get_template("index.html").render(request=request))

@app.get("/new_contact")
async def new_contact(request: Request):
    return HTMLResponse(templates.get_template("new_contact.html").render(request=request))

@app.get("/all_contacts")
async def all_contacts(request: Request):
    contacts = [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Doe", "email": "jane@example.com"}
    ]
    return HTMLResponse(templates.get_template("all_contacts.html").render(request=request, contacts=contacts))

@app.get("/all_contacts.html", response_class=HTMLResponse)
async def all_contacts_html(request: Request):
    return HTMLResponse(templates.get_template("all_contacts.html").render(request=request))
