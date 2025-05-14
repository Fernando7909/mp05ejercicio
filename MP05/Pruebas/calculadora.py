import pytest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b



def test_multiplicacion():
    assert multiplicacion (5, 2) == 10


def test_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
    assert division(5, 2) == 2.5
    assert division(9, 3) == 3



def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(10, 5) == 5
    assert resta(0, 0) == 0
