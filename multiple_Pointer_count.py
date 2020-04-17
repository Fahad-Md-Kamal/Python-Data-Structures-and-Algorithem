

def countUniqueValues(arr):
    if len(arr) == 0:
        return 0
    idx = 0
    for j in range(len(arr)):
        if arr[idx] != arr[j]:
            idx += 1
            arr[idx] = arr[j]
        print(idx,j)
    
    return idx + 1

print(countUniqueValues([1,1,2,3,3,4,5,7,8]))
# print(countUniqueValues([]))