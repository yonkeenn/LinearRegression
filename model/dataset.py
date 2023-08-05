import pandas as pd
import numpy as np
import re
import timeit


with open('./dataset/auto+mpg/auto-mpg.names') as f:
    line_clean = [line.strip() for line in f.readlines()]
    
print(line_clean[33:42])
print(re.search('[^\d][^\s]+',line_clean[33:42][2]).group(0)[1:-1])

header = [re.search('[^\d][^\s]+',i).group(0)[1:-1] for i in line_clean[33:42]]



if __name__ == "__main__":
    print(header)