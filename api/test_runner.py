import unittest
import pytest
import sys
import os
import importlib.util

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
        module_path = f"{module}.py"
        if os.path.exists(module_path):
            try:
                # Import the module using importlib
                spec = importlib.util.spec_from_file_location(module, module_path)
                imported_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(imported_module)
                
                # Add tests from the module
                suite = test_loader.loadTestsFromModule(imported_module)
                test_suite.addTest(suite)
                print(f"Successfully loaded tests from {module}")
            except Exception as e:
                print(f"Error importing {module}: {str(e)}")
        else:
            print(f"Warning: Could not find {module}.py")
    
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