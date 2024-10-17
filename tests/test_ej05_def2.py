import pytest
from src.ej05_def2 import calcula_precio


@pytest.mark.parametrize(
    "importe, iva, expected",
    [
        (1000, 1000, "El importe será de: 1210.00"),
        (1000, 18276378162, "El importe será de: 1210.00"),
        (100, 21, "El importe será de: 121.00"),
    ]
)

def test_texto_entrada(importe, iva, expected):
    assert calcula_precio(importe, iva) == expected
