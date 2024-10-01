from Clase1 import busqueda_lineal
import pytest

# Caso satisfactorio
def exito():
    lista = [10, 20, 30, 40, 50]
    objetivo = 30
    resultado = busqueda_lineal(lista, objetivo)
    assert resultado == 2