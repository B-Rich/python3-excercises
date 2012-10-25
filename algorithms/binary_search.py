from math import *

def binary_search(List, x):
    low = 0
    high = len(List) - 1
    i = 0
    while low <= high:
        if(i > 10):
            return -1
        i += 1
        mid = floor((high - low) / 2)
        print("mid: %3d high: %3d low: %3d lookup = %3d guess = %3d" % (mid, high, low, List[mid], mid + low) )
        if(List[mid] < x):
            low = mid + 1
        elif(List[mid] > x):
            high = mid - 1
        else:
            return x
    return None

print(binary_search(list(range(1, 101)), 23))
