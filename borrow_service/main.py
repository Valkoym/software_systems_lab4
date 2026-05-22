from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 5

app = FastAPI(title="Borrow Service")

BOOK_SERVICE_URL = "http://book-service:8000"


class BorrowRequest(BaseModel):
    book_id: int
    days: int


BORROWS = []


@app.post("/borrow")
def create_borrow(request: BorrowRequest):

    try:
        response = requests.get(
            f"{BOOK_SERVICE_URL}/books/{request.book_id}"
        )

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Book Service unavailable"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book_data = response.json()["book"]

    new_borrow = {
        "student_id": STUDENT_N,
        "borrow_id": len(BORROWS) + 1,
        "book": book_data["title"],
        "days": request.days,
        "status": "Borrow created"
    }

    BORROWS.append(new_borrow)

    return new_borrow


@app.get("/borrow")
def get_borrows():
    return {
        "student_id": STUDENT_N,
        "borrows": BORROWS
    }