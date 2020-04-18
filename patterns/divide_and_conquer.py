# Naive solution

# def search(arr, val):
#     for i in range(len(arr)):
#         if arr[i] == val:
#             return i
    
#     return -1

# print(search([1,5,6,7,8,9,10,11,22,55], 10))


# Refactored Solution

import math

def search(arr, val):
    minimum = 0
    maximum = len(arr)-1

    while (minimum <= maximum):
        middle = math.floor((minimum + maximum) /2)
        currentElement = arr[middle]

        # if arr[midd] < val:
        if currentElement < val:
            minimum = middle + 1
        # elif arr[midd] > val:
        elif currentElement > val:
            maximum = middle -1
        else:
            return middle

    return -1

print(search([1,5,6,7,8,9,10,11,22,55], 10))
