import pytest
from src.ej11_def import calculo


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (3, 6),
        (5, 15),
    ]
)

def test_calculo(n, expected):
    assert calculo(n) == expected