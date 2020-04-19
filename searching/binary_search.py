# states = ['Alabama', 'Alaska', 'American Samoa','Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia','Federated States of Micronesia','Florida', 'Georgia', 'Guam','Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Marshall Islands','Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands','Ohio', 'Oklahoma', 'Oregon', 'Palau','Pennsylvania', 'Puerto Rico','Rhode Island','South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Island', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# print(len(states))


# Create a function accepts sorted array and a value
# Create a left pointer at the start of the array, 
# and a right pointer at the end of the array
# While the left pointer comes before the right pointer
    # Create a pointer in the middle 
    # If you find the value you want, return the index
    # If the value is too small, move the left pointer up
    # If the value is too large, move the right pointer down
# If you never find the value, return -1

import math
def binarySearch(sortedArray, valueToFind):
    startPointer = 0
    endPointer = len(sortedArray)-1
    middlePointer = math.floor((startPointer + endPointer) / 2)
    
    while sortedArray[middlePointer] != valueToFind and startPointer <= endPointer:
        print(sortedArray[startPointer], sortedArray[middlePointer], sortedArray[endPointer])
        if valueToFind < sortedArray[middlePointer]:
            endPointer = middlePointer -1
        else:
            startPointer = middlePointer + 1
        middlePointer = math.floor((startPointer + endPointer) / 2)
    
    print(sortedArray[startPointer], sortedArray[middlePointer], sortedArray[endPointer])
    return middlePointer if sortedArray[middlePointer] == valueToFind else -1

print(binarySearch([2,5,6,9,13,15,28,30], 30))
