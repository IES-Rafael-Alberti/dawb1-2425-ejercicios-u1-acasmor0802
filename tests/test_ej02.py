import pytest
from src.ej02_def import main, introducir, calculo


@pytest.mark.parametrize(
    "precio","hora","expected",
    [
        ("10","1" , "10")
        ("10","3" , "30")
        ("40","2" , "80")
    ]
)

def test_dinero(precio, hora, expected):
    assert calculo(precio, hora) == expected