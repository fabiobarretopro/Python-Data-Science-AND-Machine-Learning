import pandas as pd
import numpy as np


def qw():
    print("="*100)


x = np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print(df)
qw()

print(df > 0)
qw()

y = df[df["W"] > 0]
print(y)
qw()

y = df[df["W"] > 0]["Y"]
print(y)
qw()

d = df[(df["W"] > 0) & (df["Y"] > 0)]
print(d)
qw()

q = df.reset_index(inplace=True)
print(df)
qw()

col = "RS RJ SP AM SC".split()

df["Estado"] = col
print(df)
qw()

r = df.set_index("Estado")
print(df)
