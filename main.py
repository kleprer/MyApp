from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()

#не придумала как заюзать и вообще как валидировать запросы, при любой попытке 
#в swagger появляется response 500 internal server error
class Read_Summary(BaseModel):
    page_title: str

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





