import pytest
from src.prueba1 import comprobación


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 3, 3),
        (3, 1, 3),
        (3, 3, 0),
    ]
)

def test_texto(num1, num2, expected):
    assert comprobación(num1, num2) == expected