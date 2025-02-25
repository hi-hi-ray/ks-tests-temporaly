"""
Load Tests avaliam o desempenho do sistema sob carga esperada. Plano para Load Tests:

1. Simular múltiplos usuários simultâneos
2. Medir tempos de resposta sob carga normal
3. Analisar consumo de recursos durante picos de uso
4. Identificar gargalos no processamento de requisições
5. Ajustar parâmetros para otimizar o desempenho
"""

import pytest
import json
from library import api

def test_load_multiple_books():
    """Test adding and retrieving multiple books"""
    test_app = api.test_client()
    
    # Add 100 books
    for i in range(100):
        isbn = f"LOAD{i:06d}"
        response = test_app.post('/books', 
                                json={"title": f"Load Test Book {i}", 
                                    "author": "Load Author", 
                                    "isbn": isbn})
        assert response.status_code == 201
    
    # Verify we can get a sample of them
    for i in range(0, 100, 10):
        isbn = f"LOAD{i:06d}"
        response = test_app.get(f'/books/{isbn}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["title"] == f"Load Test Book {i}"

if __name__ == '__main__':
    pytest.main()
