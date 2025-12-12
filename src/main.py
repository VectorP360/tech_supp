from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


books = [
    {
        "id": 2,
        "title":"книга про бизибян",
        "author":"Andey"
    },
    {
        "id":3,
        "title":"Страшное видео на 3 часа",
        "author":"ААААААаааааааааа"
    },
]


#скачивание html файла
# @app.get("/")
# def root():
#     return FileResponse("test.html", 
#                         filename="mainpage.html", 
#                         media_type="application/octet-stream")

@app.get("/")
def APIpage():
    return


# текст по определённому адресу
@app.get("/pipipopo")
def pipipopo():
    html_content = "<p3><h4>PIPI POPO</h4></p3>"
    return HTMLResponse(content=html_content)



@app.get("/books")
def bookes():
    return books


@app.get("/books/{book_id}")
def chosen_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="книги нет!")


# использование параметров
# использовать в самом конце
@app.get("/id/{id}")
def param(id):
    return  HTMLResponse(content=id)