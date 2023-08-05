import pandas as pd
import numpy as np

# importing the required modules
import timeit

# binary search function
def binary_search(mylist, find):
    print('START searching...')
    while len(mylist) > 0:
        mid = (len(mylist))//2
        print(mylist[mid])
        if mylist[mid] == find:
            return print(f'found in the {mid} position')
        elif mylist[mid] > find:
            mylist = mylist[:mid]
            print(mylist)
        else:
            mylist = mylist[mid + 1:]
            print(mylist)
    return print('Not found')

if __name__ == "__main__":
    mylist = [3,2,1,5,6,8,9,10]
    ordered_mylist = [1,2,3,4,5,6,7,8,9,10]
    binary_search(ordered_mylist, 8)