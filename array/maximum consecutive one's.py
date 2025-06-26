"""
Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of 
consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

"""

def maxConsecutiveOnes(arr):
    cnt = 0
    maxi = 0

    for n in arr:
        if n == 1:
            cnt += 1
            maxi = max(maxi, cnt)
        else:
            cnt = 0
    return maxi

l = list(map(int, input("Enter array elements: ").split()))

print(maxConsecutiveOnes(l))
