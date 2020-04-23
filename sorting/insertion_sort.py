
# Python program for implementation of Insertion Sort 

# Function to do insertion sort 
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        print(f'i = {i}, key =: {key}')
        # Jehetu i k 0 er bodole 1 theke start kora hoise tai j theke 1 baad dea loop kora hoite se.
        j = i-1
        print(f'i = {i}, Value of j  =: {j}')
        print(f'{j} >= 0: {True if j >= 0 else False}')
        print(f'{key} < {arr[j]}: {True if key < arr[j] else False}')

        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j] 
                print(f'j = {j}, arr[j+1]: {arr[j+1]} and {arr[j]}')
                j -= 1
        print(f'j = {j}, arr[j+1]: {arr[j+1]}')
        print("...")
        arr[j+1] = key
    
    return arr 


print(insertionSort([3,2,9,76,4]))