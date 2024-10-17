import pytest
from src.ej01_def import main,texto


@pytest.mark.parametrize(
    "nombre","expected",
    [
        ("Pedro","Hola Pedro")
        ("Nariz","Hola Nariz")
        ("L", "Hola L")
    ]
)

def test_hola(nombre, expected):
    assert main(nombre) == expected