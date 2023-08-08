import pandas as pd
import numpy as np
import re
import timeit


with open('./dataset/auto+mpg/auto-mpg.names') as f:
    line_clean = [line.strip() for line in f.readlines()]

with open('./dataset/auto+mpg/auto-mpg.data') as f:
    data_clean = f.readlines()

header = [re.search('[^\d][^\s]+',i).group(0)[1:-1] for i in line_clean[33:42]]
header[-1] = 'car name'
header[6] = 'model'

# Raw dataset from auto-mpg.data:

df = pd.read_fwf('./dataset/auto+mpg/auto-mpg.data', names = header)

df.horsepower.replace('?', np.nan, inplace = True)
df.horsepower = df.horsepower.astype(float)

# As we can see most of the values are related to "ford" car model, we should get the mean of this model:
ford4_mean = df[(df.cylinders == 4) & (df["car name"].str.contains('ford'))]['horsepower'].mean()
ford4_mean = round(ford4_mean, 1)

# As we can see most of the values are related to "ford" car model, we should get the mean of this model:
ford6_mean = df[(df.cylinders == 6) & (df["car name"].str.contains('ford'))]['horsepower'].mean()
ford6_mean = round(ford6_mean, 1)

# By the way, we get a general mean for  whole "cylinders = 4 and cylinders = 6":
df[(df.cylinders == 4)]['horsepower'].mean(), df[(df.cylinders == 6)]['horsepower'].mean()

# As we can see, we can use the mean of "ford" car name feature:
df.horsepower.fillna(ford4_mean, inplace = True)

if __name__ == "__main__":
    print(header)