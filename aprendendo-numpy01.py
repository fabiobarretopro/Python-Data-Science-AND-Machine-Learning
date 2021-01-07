import numpy as np


def ab():
    print("="*80)


minha_lista = [1, 2, 3]
print(np.array(minha_lista))
ab()
minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = np.array(minha_matriz)
print(x)
ab()

y = np.arange(0, 11, 2)
print(y)
ab()

teste = np.array([[np.arange(0, 11), np.arange(10, 21), np.arange(20, 31)], [np.arange(0, 11), np.arange(10, 21), np.arange(20, 31)], [np.arange(0, 11), np.arange(10, 21), np.arange(20, 31)]])
print(teste)

ab()
z = np.zeros(3)
print(z)
ab()

m = np.zeros((5, 5))
print(m)
ab()
u = np.ones((3, 3))
print(u)
ab()
print(np.eye(5))

ab()
ln = np.linspace(0, 10, 4)
print(ln)
ab()

r = np.random.rand(5)
print(r)
ab()
r = np.random.rand(5, 4)
print(r)
ab()

n = np.random.randn(4)
print(n)
ab()

rd = np.random.randint(0, 101, 10)
print(rd)

ab()

arr = np.random.rand(25)
print(arr)
ab()
print(arr.reshape((5, 5)))
ab()

print(arr.max())
ab()
print(arr.min())
ab()
print(arr.argmax())
ab()
print(arr.argmin())

