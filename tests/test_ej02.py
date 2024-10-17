import pytest
from src.ej02_def import calculo


@pytest.mark.parametrize(
    "precio, hora, expected",
    [
        (10, 1 , "El importe total es de 10."),
        (10, 3 , "El importe total es de 30."),
        (40, 2 , "El importe total es de 80."),
    ]
)

def test_dinero(precio, hora, expected):
    assert calculo(precio, hora) == expected