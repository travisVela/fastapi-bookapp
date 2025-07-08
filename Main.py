from fastapi import FastAPI, Body
from Book import Book
from BookRequest import BookRequest
app = FastAPI()

BOOKS = [
    Book(1, 'Science For Dummies', 'Jim Jimothy', "Great book", 4),
    Book(2, "Computer Stuff", "Computer Guy", "Pretty Good Book", 3),
    Book(3, "All About Sleep", "Albert Sleepyhead", "Great Book", 5),
    Book(4, 'Getting To Know Your Inner Child', 'Dorris Kid', 'Fantastic', 5)
]


@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{id}")
async def get_book_by_id(id: int):
    for book in BOOKS:
        if book.id == id:
            return book

@app.get("/books/")
async def get_books_by_rating(rating: int):
    selected_rating_books = []
    for book in BOOKS:
        if book.rating == rating:
            selected_rating_books.append(book)
    return selected_rating_books


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book