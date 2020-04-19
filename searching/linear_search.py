
# Function accepts an array and value to check
def linearSearch(arr, val):

# Loop through the array and check if the current array element is equal to the value
    for i in arr:
        
        # If it is, return the index at which the element is found
        if i == val:
            return arr.index(val)
    
    # If the value is never found, return -1    
    return -1
    
print(linearSearch([88,99,66,44,55,2,66,44,12,5,8,9,5,4], 1))0