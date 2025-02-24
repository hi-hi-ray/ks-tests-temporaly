"""
Integration Tests verificam se diferentes partes do sistema funcionam corretamente juntas. Plano para Integration Tests:

1. Testar comunicação entre módulos/componentes
2. Simular chamadas de API e verificar respostas
3. Testar interações entre banco de dados e aplicação
4. Verificar integração entre serviços externos
5. Identificar falhas na troca de dados entre partes do sistema
"""

import unittest
import json
from library import app, library

class TestLibraryIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset database before each test
        library.connection.execute("DELETE FROM books")
        library.connection.execute("DELETE FROM users")
        library.connection.execute("DELETE FROM loans")
        library.connection.commit()
    
    def test_add_book_endpoint(self):
        response = self.app.post('/books', 
                                json={"title": "Integration Test Book", 
                                    "author": "Test Author", 
                                    "isbn": "9876543210"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Integration Test Book")
        self.assertEqual(data["author"], "Test Author")
        self.assertEqual(data["isbn"], "9876543210")
        self.assertTrue(data["available"])
    
    def test_get_book_endpoint(self):
        # First add a book
        self.app.post('/books', 
                    json={"title": "Get Book Test", 
                        "author": "Test Author", 
                        "isbn": "5555555555"})
        
        # Then try to retrieve it
        response = self.app.get('/books/5555555555')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Get Book Test")
        
    def test_get_nonexistent_book_endpoint(self):
        response = self.app.get('/books/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
