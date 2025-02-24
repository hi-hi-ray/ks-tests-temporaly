from datetime import datetime, timedelta
from typing import List, Optional
import bcrypt
import sqlite3
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

class Book:
    def __init__(self, id: int, title: str, author: str, isbn: str, available: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class User:
    def __init__(self, id: int, username: str, password: str, role: str = "member"):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

class LibrarySystem:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.setup_database()
    
    def setup_database(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                isbn TEXT UNIQUE,
                available BOOLEAN
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                role TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                user_id INTEGER,
                loan_date TEXT,
                return_date TEXT,
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.connection.commit()

    def add_book(self, title: str, author: str, isbn: str) -> Book:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, isbn, available) VALUES (?, ?, ?, ?)",
            (title, author, isbn, True)
        )
        self.connection.commit()
        return Book(cursor.lastrowid, title, author, isbn)

    def get_book(self, isbn: str) -> Optional[Book]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()
        if result:
            return Book(*result)
        return None

library = LibrarySystem()

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    book = library.add_book(data["title"], data["author"], data["isbn"])
    return jsonify({"id": book.id, "title": book.title, "author": book.author, "isbn": book.isbn, "available": book.available})

@app.route("/books/<isbn>", methods=["GET"])
def get_book(isbn):
    book = library.get_book(isbn)
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "isbn": book.isbn, "available": book.available})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
