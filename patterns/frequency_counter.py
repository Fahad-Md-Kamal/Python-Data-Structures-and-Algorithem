################### { Phase one } #####################
# Frequency Checking 
def same(arr1, arr2):
    # Check the lenght of the arrays
    if len(arr1) != len(arr2):
        return False

    for i in arr1:
        if type(i) == int and i**2 in arr2:
            del arr2[arr2.index(i**2)]
        else:
            return False
    return True

print(same([1,2,3,4], [1,9,4,16]))
