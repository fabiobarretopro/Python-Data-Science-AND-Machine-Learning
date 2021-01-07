import numpy as np


def asd():
    print("="*80)


asd()
arr = np.arange(0, 30, 3)
print(arr)
asd()

print(arr[2:-2])
asd()

arr = np.arange(50).reshape(5, 10)
print(arr)
asd()
print(arr.shape)
asd()

print(arr[:3][-1])

asd()

arr2 = arr[:]
print(arr2)
asd()

print(arr[1:4, 5:])
asd()

print(arr*10 >= 250)

asd()
bol = arr*10 >= 250
print(arr[bol])

asd()

arr = np.linspace(0, 100, 30)
print(arr)

asd()
print(arr.shape)
asd()

arr = arr.reshape(3, 10)
print(arr)
asd()

print(arr[0][2])
print(arr[1][3])
asd()
print(arr[0:2, 2])