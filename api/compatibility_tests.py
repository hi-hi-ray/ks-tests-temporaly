"""
Compatibility Tests verificam se o sistema funciona corretamente em diferentes ambientes. Plano para Compatibility Tests:

1. Testar em diferentes navegadores e dispositivos
2. Validar compatibilidade com diferentes sistemas operacionais
3. Testar em diferentes resoluções de tela
4. Garantir funcionamento em diferentes versões de software
5. Verificar compatibilidade com integrações externas
"""

import unittest
import json
from library import api

class TestCompatibility(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True
    
    def test_json_content_type(self):
        # Test that the API properly handles different content type headers
        response = self.app.post('/books', 
                                json={"title": "Compatibility Test", 
                                    "author": "Test Author", 
                                    "isbn": "COMPAT123"},
                                headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 201)
    
    def test_accepts_different_json_formats(self):
        # Test that the API can handle different valid JSON formats
        response = self.app.post('/books', 
                                data=json.dumps({"title": "JSON Format Test", 
                                                "author": "Test Author", 
                                                "isbn": "FORMAT123"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
