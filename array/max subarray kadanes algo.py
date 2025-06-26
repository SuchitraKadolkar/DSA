"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
def kadanesAlgo(l):
    maxi = l[0]
    sum = 0
    for n in l:
        sum += n
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi

l = list(map(int, input("Enter array elements: ").split(" ")))

print(kadanesAlgo(l))

# Python Program to print subarray with maximum sum using Kadane's Algorithm

# Function to find the subarray with maximum sum
def maxSumSubarray(arr):
    
    # start and end of max sum subarray
    resStart = 0
    resEnd = 0
  
    # start of current subarray
    currStart = 0
  
    maxSum = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
      
        # If starting a new subarray from the current element 
        # has greater sum than extending the previous subarray
        if maxEnding + arr[i] < arr[i]:
            
            # Update current subarray sum with current element 
            # and start of current subarray with current index
            maxEnding = arr[i] 
            currStart = i
        else:
          
            # Add current element to current subarray sum
            maxEnding += arr[i]
      
        # If current subarray sum is greater than maximum subarray sum
        if maxEnding > maxSum:
          
            # Update maximum subarray sum
            maxSum = maxEnding
          
            # Update start and end of maximum sum subarray 
            resStart = currStart
            resEnd = i
  
    res = arr[resStart:resEnd + 1]
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    res = maxSumSubarray(arr)
  
    for num in res:
        print(num, end=" ")