import pandas as pd
import numpy as np

# Definimos el tamaño de la entrada y las complejidades típicas
input_sizes = [1, 10, 100, 1000, 10000]
complexities = {
    "O(1)": [1 for _ in input_sizes],  # Constante
    "O(log n)": [round(np.log2(n), 2) for n in input_sizes],  # Logarítmica
    "O(n)": [n for n in input_sizes],  # Lineal
    "O(n log n)": [round(n * np.log2(n), 2) for n in input_sizes],  # Linealítmica
    "O(n^2)": [n ** 2 for n in input_sizes],  # Cuadrática
    "O(2^n)": [2 ** n if n < 20 else 'Incalculable' for n in input_sizes],  # Exponencial
}

# Creamos el DataFrame
df = pd.DataFrame(complexities, index=input_sizes)
df.index.name = "Tamaño de entrada (n)"

# Mostramos el DataFrame
print(df)

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve el índice del elemento si lo encuentra
    return -1  # Devuelve -1 si el elemento no está en la lista


