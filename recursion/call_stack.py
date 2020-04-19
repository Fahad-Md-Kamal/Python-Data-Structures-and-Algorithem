# import math, random

# def takeShower():
#     return "Showering!"

# def eatBreakfast():
#     meal = cookFood()
#     return f'Eating {meal}'

# def cookFood():
#     items = ['Oatmeal', 'Eggs', 'Protein Shake']
#     return items[random.randint(0, len(items)-1)]

# def wakeUp():
#     print(takeShower())
#     print(eatBreakfast())
#     print("Ok...!!! Ready to go for work")

# wakeUp()


# def countDown(num):
#     if num <=  0:
#         print('All Done!')
#         return
#     print(num)
#     num -=1
#     countDown(num)

# countDown(5)


# def sumRange(num):
#     if num == 1:
#         return 1
#     return num + sumRange(num-1)

# print(sumRange(3))

# def factorial(num):
#     total = 1
#     for i in range(1,num+1):
#         total *= i
#     return total

# print(factorial(4))


# def factorialRec(num):
#     if num == 1:
#         return 1
#     return num * factorialRec(num-1)

# print(factorialRec(5))



# Recursion with helper function
# def collectOddValues(arr):
#     result = []

#     def helper(helperInput):
#         if len(helperInput) == 0:
#             return
        
#         if helperInput[0] % 2 != 0:
#             result.append(helperInput[0])

#         helper(helperInput[1:])
    
#     helper(arr)
    
#     return result

# print(collectOddValues([1,5,6,8,7,9,7,5,4,6,88,44]))


def collectOddValuesRec(arr):
    newArr = []

    if len(arr) == 0:
        return newArr
    
    if arr[0] % 2 != 0:
        newArr.append(arr[0])
    
    newArr = newArr + collectOddValuesRec(arr[1:])

    return newArr

print(collectOddValuesRec([1,5,6,8,7,9,7,5,4,6,88,44]))
