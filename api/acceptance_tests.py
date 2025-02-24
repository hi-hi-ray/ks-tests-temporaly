"""
Acceptance Tests garantem que o software atende aos requisitos do usuário. Plano para Acceptance Tests:

1. Validar que as funcionalidades principais funcionam conforme esperado
2. Testar a experiência do usuário em cenários reais
3. Garantir conformidade com os requisitos do projeto
4. Executar testes junto aos stakeholders
5. Validar fluxos completos de uso do sistema
"""

import unittest
import json
from library import app, library

class TestAcceptance(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        library.connection.execute("DELETE FROM books")
        library.connection.commit()
    
    def test_librarian_can_add_book(self):
        # Simulating a librarian adding a new book
        response = self.app.post('/books', 
                                json={"title": "New Release", 
                                    "author": "Popular Author", 
                                    "isbn": "1122334455"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "New Release")
        
        # Verify the book is in the system
        get_response = self.app.get('/books/1122334455')
        get_data = json.loads(get_response.data)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_data["title"], "New Release")

if __name__ == '__main__':
    unittest.main()
