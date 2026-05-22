from fastapi import FastAPI

STUDENT_N = 5

app = FastAPI(title="Book Service")

BOOKS = {
    501: {
        "id": 501,
        "title": "Clean Code",
        "author": "Robert Martin"
    },
    502: {
        "id": 502,
        "title": "Design Patterns",
        "author": "GoF"
    }
}


@app.get("/books")
def get_books():
    return {
        "student_id": STUDENT_N,
        "books": list(BOOKS.values())
    }


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id in BOOKS:
        return {
            "student_id": STUDENT_N,
            "book": BOOKS[book_id]
        }

    return {
        "error": "Book not found"
    }