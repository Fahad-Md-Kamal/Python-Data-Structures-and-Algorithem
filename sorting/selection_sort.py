# - Store the first element as the smallest value you've seen so far.
# - Compare this item to the next item in the array until you find a smaller number
# - If a smaller number is found, designate the smaller 
#   number to be the new minimum an continue until the end of the array
# - If the minimum is not the value (index) you initially began with, swap the two values.
 


# def selection_sort(L):
#     # i indicates how many items were sorted
#     for i in range(len(L)-1):
#         # To find the minimum value of the unsorted segment
#         # We first assume that the first element is the lowest
#         min_index = i
#         # We then use j to loop through the remaining elements
#         for j in range(i+1, len(L)-1):
#             # Update the min_index if the element at j is lower than it
#             if L[j] < L[min_index]:
#                 min_index = j
#         # After finding the lowest item of the unsorted regions, swap with the first unsorted item
#         L[i], L[min_index] = L[min_index], L[i]
#     return L

# print(selection_sort([3, 1, 41, 59, 26, 53, 59]))



# def selectionSort(arr):

#     for i in range(len(arr)):
#         lowest = i
#         for j in range(i+1 , len(arr)):
#             if arr[j] < arr[lowest]:
#                 lowest = j
#             arr[i], arr[lowest] = arr[lowest], arr[i]
#     return arr

# print(selectionSort([34,22,10,19,17]))    

