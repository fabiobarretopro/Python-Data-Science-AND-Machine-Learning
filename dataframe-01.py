import pandas as pd
import numpy as np


def qw():
    print("="*100)


x = np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print(df)
qw()

print(df["W"])
qw()

print(df[["W", "Z"]])
qw()

df["new"] = df["W"] + df["X"]
print(df)
qw()


df.drop("new", axis=1, inplace=True)
print(df)
qw()

z = df.loc["A", "W"]
print(z)
qw()
y = df.loc[["A", "B"], ["X", "Y"]]
print(y)
qw()

z = df.iloc[1:4, 2:]
print(z)
qw()



