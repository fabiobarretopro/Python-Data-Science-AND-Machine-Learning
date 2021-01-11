import numpy as np
import pandas as pd

label = ["a", "b", "c"]
minha_lista = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {"a": 10, "b": 20, "c": 30}

series = pd.Series(data=minha_lista, index=label)
print(series)
print(series["b"])

y = pd.Series([sum, print, len])
print(y)

ser1 = pd.Series([1, 2, 3, 4], index=["EUA", "Alemanha", "Rússia", "Japão"])
print(ser1)

ser2 = pd.Series([1, 2, 3, 4], index=["EUA", "Alemanha", "Itália", "Japão"])
print(ser2)

print(ser1 + ser2)

