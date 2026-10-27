
from greeting import greet

def test_greet():
    assert greet("Huzaifa") == "Hello, Huzaifa! Welcome to our application."

def test_greet_another_user():
    assert greet("Ali") == "Hello, Ali! Welcome to our application."
