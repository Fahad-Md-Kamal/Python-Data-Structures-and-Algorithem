# def swap(arr, idx1, idx2):
#     tmp = arr[idx1]
#     arr[idx1] = arr[idx2]
#     arr[idx2] = tmp

# def bubbleSort(arr):
#     lngth = len(arr) -1
#     srted = False
#     while not srted:
#         srted = True
#         for i in range(0, lngth):
#             print(arr[i], arr[i + 1])
#             if arr[i] > arr[i + 1]:
#                 srted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#             print(arr)
#     return arr

    
# This is log(n) complexity
# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
    noSwap = True
    # Traverse through all array elements
    for i in range(n):
        noSwap = True
        # Last i elements are already in place
        for j in range(0, n-i-1):
            print(arr, arr[j] , arr[j+1] )
            if arr[j] > arr[j+1] :
                noSwap = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"{i} Item Sorted")
        if noSwap == True:
            break
    return arr

print("############### 3 item ####################")
print(bubbleSort([88, 1, 4, 9, 3, 5, 6]))
print("################ 2 Item ###################")
print(bubbleSort([8, 1, 9, 4, 5, 6]))
