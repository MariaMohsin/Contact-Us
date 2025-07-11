
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agents import Agent, AsyncOpenAI,OpenAIChatCompletionsModel,Runner


app = FastAPI()
templates = Jinja2Templates(directory="templates")



# Contact form route
@app.get("/", response_class=HTMLResponse)
async def contact_form(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    # ✅ All variables used in message
    confirmation = (
        f"Thanks {name}, we received your message: \"{message}\". "
        f"We’ll get back to you at {email} soon!"
    )

    # You can also log to console (optional)
    print("📬 Contact Form Submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return templates.TemplateResponse("contact.html", {
        "request": request,
        "confirmation": confirmation
    })
