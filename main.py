from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()

#не придумала как заюзать и вообще как валидировать запросы, при любой попытке ниже
#в swagger появляется response 500 internal server error
class Read_Summary(BaseModel):
    page_title: str
    page_summary: str

class Page_Url(BaseModel):
    page_title: str
    page_url: str

class Get_Image(BaseModel):
    page_title: str
    image_url: str


#попытка валидации (неудачная)
#@app.get("/{page_title}", response_model = Read_Summary)
#def get_summary(page_summary: Read_Summary):
#    return Read_Summary(page_title = page_summary.page_title, page_summary = wikipedia.summary(page_title))

@app.get("/{page_title}")
def get_summary(page_title: str):
    return wikipedia.summary(page_title)

#попытка валидации (неудачная)
#@app.get("/", response_model = Page_Url)
#def get_page_url(page_url: Page_Url):
#    return Page_Url(page_title = page_url.page_title, page_url = wikipedia.page(page_url.page_title).images[0])

@app.get("/")
def get_page_url(page_title: str):
    return wikipedia.page(page_title).url

@app.post("/", response_model=Get_Image)
def image(get_image: Get_Image):
    return Get_Image(page_title=get_image.page_title, image_url=wikipedia.page(get_image.page_title).images[0])



#по адресу http://127.0.0.1:8000/ выдает ошибку, не разобралась, как ее решить:
#{
#    "detail": [
#        {
#            "type": "missing",
#            "loc": [
#                "query",
#                "page_title"
#            ],
#            "msg": "Field required",
#            "input": null,
#            "url": "https://errors.pydantic.dev/2.4/v/missing"
#        }
#    ]
#}

