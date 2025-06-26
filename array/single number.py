"""
Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single 
one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

Solution:
xor of number with itself results in zero. So calculating xor of all array elements results in single number.
"""

def singleNumber(nums):
    xor_nums = 0
    for i in range(len(nums)):
        xor_nums = xor_nums ^ nums[i]
    return xor_nums

l = list(map(int, input("Enter array elements: ").split()))

print(singleNumber(l))