# test_ci.py

def test_print_hello_world():
    print("Hello, World!")
    assert True

def test_print_ci_pass():
    print("CI Pipeline Test Passed!")
    assert True

def test_print_pytest():
    print("Pytest is working correctly!")
    assert True