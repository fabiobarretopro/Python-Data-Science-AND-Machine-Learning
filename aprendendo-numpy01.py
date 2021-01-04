import numpy as np

"""minha_lista = [1, 2, 3]

x = np.array(minha_lista)
print(x)
print("="*30)
minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = np.array(minha_matriz)
print(x)"""

print(np.arange(0, 10, 2))
print("="*30)
print(np.zeros(5))
print("="*30)
arr = np.zeros((5, 5))
print(arr)
print("="*30)
ari = np.ones((4, 4))
print(ari)
print("="*30)

x = np.eye(4)
print(x)
print("="*30)
y = np.linspace(0, 10, 3)
print(y)

print("="*30)

z = np.random.rand(4, 4, 3)
print(z)
print("="*30)
print("="*30)
z = np.random.randn(4, 5)
print(z)
print("="*30)

w = np.random.randint(0, 100, 10)
print(w)
print("="*30)
arr = np.random.rand(25)
print(arr)
print("="*30)

print(arr.reshape(5, 5))

print("="*30)

print(arr.max())
print(arr.min())
print("="*30)
print(arr.argmax())
print(arr.argmin())