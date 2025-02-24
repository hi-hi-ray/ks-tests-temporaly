import unittest
import pytest
import sys
import os

def run_all_tests():
    """Run all test types"""
    # Standard unittest tests
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    
    # Load all test modules
    test_modules = [
        'unit_tests',
        'integration_tests',
        'smoke_tests',
        'acceptance_tests',
        'security_tests',
        'regression_tests',
        'usability_tests',
        'compatibility_tests',
        'system_tests',
        'performance_tests'
    ]
    
    for module in test_modules:
        try:
            # Import the module
            imported_module = __import__(module)
            # Add tests from the module
            suite = test_loader.loadTestsFromModule(imported_module)
            test_suite.addTest(suite)
        except ImportError:
            print(f"Warning: Could not import {module}")
    
    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Run pytest tests
    pytest_modules = [
        'load_tests.py',
        'stress_tests.py',
        'scalability_tests.py',
        'exploratory_tests.py'
    ]
    
    for module in pytest_modules:
        if os.path.exists(module):
            print(f"\nRunning pytest tests from {module}")
            pytest.main(['-v', module])
        else:
            print(f"Warning: Could not find {module}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
