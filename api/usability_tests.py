"""
Usability Tests avaliam a experiência do usuário ao interagir com o sistema. Plano para Usability Tests:

1. Testar a interface com usuários reais
2. Medir facilidade de uso e navegação
3. Observar dificuldades encontradas pelos usuários
4. Coletar feedback sobre a experiência
5. Melhorar o design com base nos resultados
"""

import unittest
import json
from library import app

class TestUsability(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_error_message_clarity(self):
        # Test that the error message for a non-existent book is clear
        response = self.app.get('/books/nonexistent')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", data)
        self.assertEqual(data["error"], "Book not found")

if __name__ == '__main__':
    unittest.main()
