"""
Scalability Tests verificam a capacidade do sistema de lidar com aumento de demanda. Plano para Scalability Tests:

1. Testar a escalabilidade horizontal e vertical
2. Avaliar o desempenho com aumento progressivo de carga
3. Identificar limites de escalabilidade
4. Simular crescimento de usuários e tráfego
5. Medir impacto de novas instâncias ou recursos adicionais
"""

import os
import tempfile
from datetime import datetime, timedelta
import pytest
from library import LibrarySystem

def test_database_size_impact():
    """Test how the system performs with a larger database"""
    # Create a temporary database file
    fd, path = tempfile.mkstemp()
    os.close(fd)  # Close the file descriptor immediately
    
    try:
        # Initialize a new library system with the file
        test_lib = LibrarySystem(path)
        
        # Add 1000 books
        for i in range(1000):
            isbn = f"SCALE{i:06d}"
            test_lib.add_book(f"Scalability Test Book {i}", "Scale Author", isbn)
        
        # Test retrieval time for first, middle, and last book
        start_time = datetime.now()
        first_book = test_lib.get_book("SCALE000000")
        mid_book = test_lib.get_book("SCALE000500")
        last_book = test_lib.get_book("SCALE000999")
        end_time = datetime.now()
        
        # Verify all books were retrieved correctly
        assert first_book is not None
        assert mid_book is not None
        assert last_book is not None
        
        # Check that retrieval time is reasonable (less than 1 second)
        assert (end_time - start_time) < timedelta(seconds=1)
        
        # Explicitly close the connection before deleting the file
        test_lib.connection.close()
        
    finally:
        # Make sure the file is removed even if tests fail
        try:
            os.unlink(path)
        except PermissionError:
            # If we still can't delete it, just log the issue
            print(f"Warning: Could not delete temporary file {path}")

if __name__ == '__main__':
    pytest.main()