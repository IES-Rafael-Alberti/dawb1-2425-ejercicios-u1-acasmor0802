import pytest
from src.ej01_def import texto


@pytest.mark.parametrize(
    "nombre, expected",
    [
        ("Pedro","Hola Pedro"),
        ("Nariz","Hola Nariz"),
        ("L", "Hola L"),
    ]
)

def test_texto(nombre, expected):
    assert texto(nombre) == expected