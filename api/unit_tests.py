"""
Unit Tests são testes automatizados que verificam o funcionamento de unidades individuais do código, como funções ou métodos isolados. Aqui está um plano para Unit Tests:

1. Testar cada função/método individualmente com diferentes entradas esperadas
2. Garantir que exceções sejam tratadas corretamente
3. Mockar dependências para isolar a unidade testada
4. Cobrir casos de borda e valores extremos
5. Executar frequentemente para evitar regressões
"""

import unittest
import json
from library import api, Book, User, LibrarySystem, library
from flask import app
from unittest.mock import patch, MagicMock

class TestBookClass(unittest.TestCase):
    def test_book_creation(self):
        book = Book(1, "Test Title", "Test Author", "1234567890", True)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.isbn, "1234567890")
        self.assertTrue(book.available)

class TestUserClass(unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "testuser", "password123", "member")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.role, "member")
    
    def test_default_role(self):
        user = User(1, "testuser", "password123")
        self.assertEqual(user.role, "member")

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = LibrarySystem(":memory:")
    
    def test_add_book(self):
        book = self.library.add_book("Test Book", "Test Author", "1234567890")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.isbn, "1234567890")
        self.assertTrue(book.available)
    
    def test_get_book(self):
        self.library.add_book("Test Book", "Test Author", "1234567890")
        book = self.library.get_book("1234567890")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Book")
        
    def test_get_nonexistent_book(self):
        book = self.library.get_book("nonexistent")
        self.assertIsNone(book)

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True

    @patch.object(library, 'add_book')
    def test_add_book(self, mock_add_book):
        mock_add_book.return_value = MagicMock(id=1, title="Test Book", author="Author", isbn="123456789", available=True)
        
        response = self.app.post("/books", json={
            "title": "Test Book",
            "author": "Author",
            "isbn": "123456789"
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Book", response.get_data(as_text=True))
    
    @patch.object(library, 'get_book')
    def test_get_book(self, mock_get_book):
        mock_get_book.return_value = MagicMock(id=1, title="Test Book", author="Author", isbn="123456789", available=True)
        
        response = self.app.get("/books/123456789")
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Book", response.get_data(as_text=True))

    @patch.object(library, 'get_book')
    def test_get_book_not_found(self, mock_get_book):
        mock_get_book.return_value = None
        
        response = self.app.get("/books/000000000")
        
        self.assertEqual(response.status_code, 404)
        self.assertIn("Book not found", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
