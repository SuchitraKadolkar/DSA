"""
Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the 
majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Solution:
Brute approach is to use hashmap and store count of occurence of every element in an array.
    Then return the element having maximun count value.
Optimal approach is to sort the array and simply return the mid element of the array.
"""
def majorityElement(nums):
    """
    mp = {}
    for i in nums:
        mp[i] = mp.get(i, 0)+1
    return max(mp, key=mp.get)
    """
    nums.sort()
    mid = len(nums) // 2
    return nums[mid]

l = list(map(int, input("Enter array elements: ").split()))

print(majorityElement(l))