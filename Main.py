from fastapi import FastAPI, Path, Query, HTTPException
from Book import Book
from BookRequest import BookRequest
from starlette import status
app = FastAPI()

BOOKS = [
    Book(1, 'Science For Dummies', 'Jim Jimothy', "Great book", 4, 2022),
    Book(2, "Computer Stuff", "Computer Guy", "Pretty Good Book", 3, 1999),
    Book(3, "All About Sleep", "Albert Sleepyhead", "Great Book", 5, 2022),
    Book(4, 'Getting To Know Your Inner Child', 'Dorris Kid', 'Fantastic', 5, 2012)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS

@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/rating/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating: int = Query(gt=0,lt=6)):
    books_by_rating = []
    for book in BOOKS:
        if book.rating == rating:
            books_by_rating.append(book)
    return books_by_rating

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_books_by_year(year: int = Query(gt=1999,lt=2026)):
    books_by_year = []
    for book in BOOKS:
        if book.published_date == year:
            books_by_year.append(book)
    return books_by_year

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_updated = True
    if not book_updated:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")