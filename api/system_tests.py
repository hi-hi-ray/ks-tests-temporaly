"""
System Tests avaliam o sistema como um todo, verificando sua conformidade com os requisitos. Plano para SYSTEM Tests:

1. Testar todas as funcionalidades do sistema
2. Validar requisitos funcionais e não funcionais
3. Garantir integração correta entre componentes
4. Simular cenários de uso reais
5. Certificar que o sistema atende aos critérios de aceitação
"""

import unittest
import json
from library import api, library

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True
        # Reset database
        library.connection.execute("DELETE FROM books")
        library.connection.commit()
    
    def test_end_to_end_book_management(self):
        # Add a new book
        add_response = self.app.post('/books', 
                                    json={"title": "System Test Book", 
                                        "author": "System Author", 
                                        "isbn": "SYSTEM123"})
        self.assertEqual(add_response.status_code, 201)
        
        # Retrieve the book
        get_response = self.app.get('/books/SYSTEM123')
        self.assertEqual(get_response.status_code, 200)
        get_data = json.loads(get_response.data)
        self.assertEqual(get_data["title"], "System Test Book")

if __name__ == '__main__':
    unittest.main()
