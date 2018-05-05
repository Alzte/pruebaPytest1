import pytest
import principal


def testSuma():
    total = principal.suma(2, 3)
    assert total == 5


def testMultiplicacion():
    total = principal.multiplicacion(1, 2)
    assert total == 2
