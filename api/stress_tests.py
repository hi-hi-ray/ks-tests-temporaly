"""
Stress Tests testam o sistema em condições extremas. Plano para Stress Tests:

1. Aumentar a carga progressivamente até o sistema falhar
2. Medir comportamento sob uso intenso
3. Testar limites de conexões simultâneas
4. Monitorar tempo de resposta sob sobrecarga
5. Identificar pontos fracos e falhas críticas
"""

import time
import pytest
from library import api

def test_concurrent_book_additions():
    """Test performance under stress without benchmark"""
    test_app = api.test_client()
    
    # Measure time manually
    start_time = time.time()
    
    # Add multiple books
    for i in range(20):
        isbn = f"STRESS{i:06d}"
        response = test_app.post('/books', 
                        json={"title": f"Stress Test Book {i}", 
                            "author": "Stress Author", 
                            "isbn": isbn})
        assert response.status_code == 201
        
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Check that adding 20 books takes reasonable time
    assert execution_time < 5.0, f"Adding 20 books took {execution_time} seconds, which exceeds the 5-second threshold"
    
    print(f"Performance: Added 20 books in {execution_time:.2f} seconds")

@pytest.mark.benchmark
def test_concurrent_book_additions_with_benchmark(benchmark):
    def add_books():
        test_app = api.test_client()
        for i in range(20):
            isbn = f"STRESS{i:06d}"
            test_app.post('/books', 
                        json={"title": f"Stress Test Book {i}", 
                            "author": "Stress Author", 
                            "isbn": isbn})
    
    # This will run the function multiple times and measure performance
    benchmark(add_books)

if __name__ == '__main__':
    pytest.main()