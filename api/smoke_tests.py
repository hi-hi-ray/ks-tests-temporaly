"""
Smoke Tests são verificações rápidas para garantir que as funcionalidades principais de um sistema estão operacionais. Plano para SMOKE Tests:

1. Verificar se o sistema inicializa corretamente
2. Testar as principais rotas da API
3. Confirmar que a interface do usuário carrega sem erros
4. Validar que o banco de dados está acessível
5. Executar testes em ambientes de desenvolvimento e produção
"""


import unittest
from library import api

class TestSmoke(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True
    
    def test_server_running(self):
        response = self.app.get('/')
        # Even if it's a 404, we want to make sure the server is running
        self.assertIn(response.status_code, [200, 404])
    
    def test_basic_book_operations(self):
        # Add a book
        add_response = self.app.post('/books', 
                                    json={"title": "Smoke Test Book", 
                                        "author": "Smoke Author", 
                                        "isbn": "1111222233"})
        self.assertEqual(add_response.status_code, 201)
        
        # Retrieve the book
        get_response = self.app.get('/books/1111222233')
        self.assertEqual(get_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
