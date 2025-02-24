"""
Testes exploratórios são tipicamente testes manuais onde os testadores exploram o sistema
para encontrar comportamentos inesperados. Aqui está um plano para testes exploratórios:

1. Tente adicionar livros com caracteres especiais em títulos/autores
2. Tente adicionar livros com títulos/autores/ISBNs muito longos
3. Tente adicionar o mesmo livro duas vezes
4. Tente vários casos extremos para formatos de ISBN
5. Explore a API sem seguir os padrões de uso esperados
6. Tente quebrar o sistema com entradas inesperadas

Esses testes seriam realizados manualmente ou com scripts específicos projetados
para sondar comportamentos inesperados.
"""

import json
import pytest
from library import api

def exploratory_test_special_characters():
    test_app = api.test_client()
    # Test special characters in book fields
    response = test_app.post('/books', 
                            json={"title": "Special Characters: !@#$%^&*()", 
                                "author": "Author with ♥ and ∞ symbols", 
                                "isbn": "SPECIAL123"})
    assert response.status_code == 200
    
    # Verify retrieval works
    get_response = test_app.get('/books/SPECIAL123')
    assert get_response.status_code == 200
    data = json.loads(get_response.data)
    assert data["title"] == "Special Characters: !@#$%^&*()"
    assert data["author"] == "Author with ♥ and ∞ symbols"

def exploratory_test_long_fields():
    test_app = api.test_client()
    # Test extremely long book title and author
    very_long_title = "A " + "very " * 100 + "long title"
    very_long_author = "An " + "extremely " * 100 + "verbose author name"
    
    response = test_app.post('/books', 
                            json={"title": very_long_title, 
                                "author": very_long_author, 
                                "isbn": "LONG12345"})
    
    # Check if system handles long fields
    assert response.status_code == 200
    
    # Verify retrieval works with long fields
    get_response = test_app.get('/books/LONG12345')
    assert get_response.status_code == 200

def exploratory_test_duplicate_isbn():
    test_app = api.test_client()
    # Add a book
    test_app.post('/books', 
                json={"title": "Original Book", 
                    "author": "Original Author", 
                    "isbn": "DUPLICATE1"})
    
    # Try to add another book with the same ISBN
    response = test_app.post('/books', 
                            json={"title": "Duplicate Book", 
                                "author": "Another Author", 
                                "isbn": "DUPLICATE1"})
    
    # This should fail due to unique constraint on ISBN
    # Note: The current implementation might not properly handle this case
    # So we're checking both possibilities
    assert response.status_code in [400, 500]

if __name__ == '__main__':
    pytest.main()
