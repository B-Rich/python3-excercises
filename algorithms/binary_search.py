from math import *

def binary_search(List, x):
    low = 0
    high = len(List) - 1
    while low <= high:
        mid = int((high + low) / 2)
        print("mid: %3d high: %3d low: %3d lookup = %3d guess = %3d float = %3f" % (mid, high, low, List[mid], mid + low, (high + low) / 2.0) )
        if List[mid] < x:
            low = mid
        elif List[mid] > x:
            high = mid
        else:
            return mid
    return None

print(binary_search(list(range(1, 103421)), 7345))
