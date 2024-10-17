import pytest
from src.ej04_def2 import grados_celsius


@pytest.mark.parametrize(
    "farenheit, expected",
    [
        (32, 0.0),
        (33.8, 1.0),
    ]
)

def test_texto_entrada(farenheit, expected):
    assert grados_celsius(farenheit) == expected

