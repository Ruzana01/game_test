# from lesson1 import add, substract, multiply, divide

# assert add(10, 5) == 15
# assert substract(10, 5) == 5
# assert multiply(10, 5) == 50
# assert divide(10, 0) == 2

import pytest
from lesson1 import add, substract, multiply, divide

def test_add():
    assert add(10, 5) == 15

def test_substract():
    assert substract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    
