"""
Regression Tests garantem que novas alterações não quebrem funcionalidades existentes. Plano para Regression Tests:

1. Executar testes automatizados em cada nova versão
2. Verificar se funcionalidades antigas continuam funcionando
3. Garantir que correções de bugs não introduzam novos erros
4. Testar componentes afetados por mudanças recentes
5. Manter um conjunto robusto de testes de regressão
"""

import unittest
import json
from library import app

class TestRegression(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Add a book that we'll use for regression testing
        self.app.post('/books', 
                    json={"title": "Regression Test Book", 
                        "author": "Regression Author", 
                        "isbn": "REGR12345"})
    
    def test_book_retrieval_after_changes(self):
        # This test ensures that book retrieval still works after code changes
        response = self.app.get('/books/REGR12345')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["title"], "Regression Test Book")
        self.assertEqual(data["author"], "Regression Author")

if __name__ == '__main__':
    unittest.main()
