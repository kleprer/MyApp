from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()

class Get_Image(BaseModel):
    page_title: str
    image_url: str


@app.get("/{page_title}")
def get_summary(page_title: str):
    return wikipedia.summary(page_title)

@app.get("/")
def get_page_url(page_title: str):
    return wikipedia.page(page_title).url

@app.post("/", response_model=Get_Image)
def image(get_image: Get_Image):
    return Get_Image(page_title=get_image.page_title, image_url=wikipedia.page(get_image.page_title).images[0])
