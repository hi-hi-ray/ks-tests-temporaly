import unittest
import json
import os
import tempfile
from datetime import datetime, timedelta
import pytest
from library import app, library, Book, User, LibrarySystem

# UNIT TESTS


# INTEGRATION TESTS
class TestLibraryIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset database before each test
        library.connection.execute("DELETE FROM books")
        library.connection.execute("DELETE FROM users")
        library.connection.execute("DELETE FROM loans")
        library.connection.commit()
    
    def test_add_book_endpoint(self):
        response = self.app.post('/books', 
                                json={"title": "Integration Test Book", 
                                    "author": "Test Author", 
                                    "isbn": "9876543210"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Integration Test Book")
        self.assertEqual(data["author"], "Test Author")
        self.assertEqual(data["isbn"], "9876543210")
        self.assertTrue(data["available"])
    
    def test_get_book_endpoint(self):
        # First add a book
        self.app.post('/books', 
                    json={"title": "Get Book Test", 
                        "author": "Test Author", 
                        "isbn": "5555555555"})
        
        # Then try to retrieve it
        response = self.app.get('/books/5555555555')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Get Book Test")
        
    def test_get_nonexistent_book_endpoint(self):
        response = self.app.get('/books/nonexistent')
        self.assertEqual(response.status_code, 404)

# SMOKE TESTS
class TestSmoke(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
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
        self.assertEqual(add_response.status_code, 200)
        
        # Retrieve the book
        get_response = self.app.get('/books/1111222233')
        self.assertEqual(get_response.status_code, 200)

# ACCEPTANCE TESTS
class TestAcceptance(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset database before each test
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

# LOAD TESTS
def test_load_multiple_books():
    """Test adding and retrieving multiple books"""
    test_app = app.test_client()
    
    # Add 100 books
    for i in range(100):
        isbn = f"LOAD{i:06d}"
        response = test_app.post('/books', 
                                json={"title": f"Load Test Book {i}", 
                                    "author": "Load Author", 
                                    "isbn": isbn})
        assert response.status_code == 200
    
    # Verify we can get a sample of them
    for i in range(0, 100, 10):
        isbn = f"LOAD{i:06d}"
        response = test_app.get(f'/books/{isbn}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["title"] == f"Load Test Book {i}"

# STRESS TESTS
def test_concurrent_book_additions(benchmark):
    """Benchmark to test performance under stress"""
    def add_books():
        test_app = app.test_client()
        for i in range(20):
            isbn = f"STRESS{i:06d}"
            test_app.post('/books', 
                        json={"title": f"Stress Test Book {i}", 
                            "author": "Stress Author", 
                            "isbn": isbn})
    
    # This will run the function multiple times and measure performance
    benchmark(add_books)

# SECURITY TESTS
class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
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

# REGRESSION TESTS
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

# USABILITY TESTS (would typically involve human testers, but we can simulate some aspects)
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

# COMPATIBILITY TESTS
class TestCompatibility(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_json_content_type(self):
        # Test that the API properly handles different content type headers
        response = self.app.post('/books', 
                                json={"title": "Compatibility Test", 
                                    "author": "Test Author", 
                                    "isbn": "COMPAT123"},
                                headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)
    
    def test_accepts_different_json_formats(self):
        # Test that the API can handle different valid JSON formats
        response = self.app.post('/books', 
                                data=json.dumps({"title": "JSON Format Test", 
                                                "author": "Test Author", 
                                                "isbn": "FORMAT123"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

# SYSTEM TESTS
class TestSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
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
        self.assertEqual(add_response.status_code, 200)
        
        # Retrieve the book
        get_response = self.app.get('/books/SYSTEM123')
        self.assertEqual(get_response.status_code, 200)
        get_data = json.loads(get_response.data)
        self.assertEqual(get_data["title"], "System Test Book")

# SCALABILITY TESTS
def test_database_size_impact():
    """Test how the system performs with a larger database"""
    # Create a temporary database file
    fd, path = tempfile.mkstemp()
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
        
    finally:
        os.close(fd)
        os.unlink(path)

# PERFORMANCE TESTS
class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_response_time(self):
        # Test that adding a book and retrieving it happens within a reasonable time
        start_time = datetime.now()
        
        # Add a book
        self.app.post('/books', 
                    json={"title": "Performance Test", 
                        "author": "Performance Author", 
                        "isbn": "PERF12345"})
        
        # Retrieve the book
        self.app.get('/books/PERF12345')
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # Check that both operations together take less than 1 second
        self.assertLess(execution_time, 1.0)

# EXPLORATORY TESTS
"""
Exploratory tests are typically manual tests where testers explore the system
to find unexpected behaviors. Here's a plan for exploratory testing:

1. Try adding books with special characters in titles/authors
2. Try adding books with very long titles/authors/ISBNs
3. Try adding the same book twice
4. Try various edge cases for ISBN formats
5. Explore the API without following the expected usage patterns
6. Try to break the system with unexpected inputs

These tests would be performed manually or with specific scripts designed
to probe for unexpected behaviors.
"""

def exploratory_test_special_characters():
    test_app = app.test_client()
    # Test special characters in book fields
    response = test_app.post('/books', 
                            json={"title": "Special Characters: !@#$%^&*()", 
                                "author": "Author with ♥ and ∞ symbols", 
                                "isbn": "SPECIAL123"})
    assert response.status_code == 200
    
    # Verify retrieval works
    get_response = test_app.get('/books/SPECIAL123')
    assert get_response.status_code == 200
    data = json.loads(get_response.data)
    assert data["title"] == "Special Characters: !@#$%^&*()"
    assert data["author"] == "Author with ♥ and ∞ symbols"

if __name__ == '__main__':
    unittest.main()