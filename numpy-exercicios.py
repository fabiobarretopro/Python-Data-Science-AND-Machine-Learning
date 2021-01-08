import numpy as np


def qw():
    print("="*80)


zero = np.zeros(10)
print(zero)
qw()
one = np.ones(10)
print(one)
qw()
zeros = np.zeros(10) + 5
print(zeros)
qw()
inteiros = np.arange(10, 51)
print(inteiros)
qw()
pares = np.arange(10, 51, 2)
print(pares)
qw()
matriz = np.arange(0, 9).reshape(3, 3)
print(matriz)
qw()

iden = np.eye(3)
print(iden)
qw()

num = np.random.rand(1)
print(num)
qw()
nor = np.random.randn(25)
print(nor)
qw()
tam = np.arange(0, 101)/100
print(tam)
qw()
z = np.linspace(0, 1, 20)
print(z)
qw()

mat = np.arange(1, 26).reshape(5, 5)
print(mat)
qw()
mat2 = mat[2:, 1:]
print(mat2)
qw()

mat3 = mat[3][4]
print(mat3)
qw()
mat4 = mat[:3, 1:2]
print(mat4)
qw()
mat5 = mat[4:, :]
print(mat5)
qw()
mat6 = mat[3:, :]
print(mat6)
qw()
soma = np.sum(mat)
print(soma)
qw()
des = np.std(mat)
print(des)
qw()
col = mat.sum(axis=0)
print(col)
