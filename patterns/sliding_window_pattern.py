

# def maxSubarraySum(arr, num):
#     if num > len(arr):
#         return None
    
#     mx =  -infinity
#     for i in range(len(arr)):
#         temp = 0
#         for j in range(num):
#             temp += arr[i+j]
#         if temp > mx:
#             mx = temp
#     return mx


# def maxSubarraySum(arr, num):
#     mxSum = 0
#     tempSum = 0
#     if len(arr) < num:
#         return None
    
#     # mx = -infinity
#     for i in range(len(arr)):
#         mxSum += arr[i]
    
#     tempSum = mxSum
#     for i in range(len(arr)):
#         tempSum = tempSum - arr[i - num] + arr[i]
#         mxSum = max(mxSum, tempSum)
#         print(tempSum, mxSum)
#     return mxSum



# print(maxSubarraySum([2,6,0,2,1,8,5,6,3], 3))