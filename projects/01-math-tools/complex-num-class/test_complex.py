import pytest
from main import Complex

def test_init():
    z = Complex(1, 2)
    assert z.real == 1
    assert z.imag == 2

def test_add():
    z1 = Complex(1, 2)
    z2 = Complex(2, 3)

    result = z1 + z2

    # (1 + 2), (2 + 3) = 3, 5
    assert result == Complex(3, 5)

def test_mul():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)

    result = z1 * z2

    # (1*3 - 2*4) + (1*4 + 2*3)i 
    # (3 - 8) + (4 + 6)i = -5 + 10i
    assert result == Complex(-5, 10)

def test_mul_negative():
    z1 = Complex(1, -1)
    z2 = Complex(1, 1)

    result = z1 * z2

    # (1*1 - -1*1) + (1*1 + -1*1)i 
    # (1 - -1) + (1 + -1)i = 2 + 0i
    assert result == Complex(2, 0)

def test_rep():
    z = Complex(5, 6)

    assert repr(z) == "Complex(5, 6i)"

