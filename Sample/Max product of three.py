"""
Maximum Product of Three Numbers
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""

def maximumProduct(nums):
    nums.sort()
    last_product = nums[-1]*nums[-2]*nums[-3]
    first_product = nums[0]*nums[1]*nums[-1]
    return max(last_product, first_product)

arr = [int(x) for x in input("Enter array elements: ").split()]

print(maximumProduct(arr))