#source .venv/Scripts/activate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


posts : list[dict] =[
        {
            "id": 1,
            "title": "Getting Started with FastAPI",
            "summary": "Learn how to build web applications with FastAPI.",
            "img": "blog_1.jpg",
            "date": "08 June 2026"
        },
        {
            "id": 2,
            "title": "Understanding Jinja2 Templates",
            "summary": "Create dynamic HTML pages using Jinja2.",
            "img": "blog_2.jpg",
            "date": "07 June 2026"
        }
    ]

@app.get("/", include_in_schema=False)
@app.get("/posts",include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"posts": posts}  # request is now separate, not inside context
    )

@app.get("/api/posts")
def get_posts():
    return posts