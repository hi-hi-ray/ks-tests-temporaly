"""
Security Tests garantem que o sistema esteja protegido contra vulnerabilidades. Plano para Security Tests:

1. Testar injeção de SQL e outras vulnerabilidades comuns
2. Verificar segurança de autenticação e autorização
3. Avaliar proteção contra ataques DDoS
4. Identificar exposição de dados sensíveis
5. Testar segurança de APIs e comunicações
"""

import unittest
from library import api

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True
    
    def test_sql_injection_prevention(self):
        # Try to inject SQL in the ISBN parameter
        response = self.app.get('/books/1234" OR "1"="1')
        # This should return a 404 not found rather than executing the injected SQL
        self.assertEqual(response.status_code, 404)
    
    def test_invalid_json(self):
        # Send invalid JSON to the add book endpoint
        response = self.app.post('/books', 
                                data="This is not JSON",
                                content_type='application/json')
        # This should return a 400 Bad Request
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
