"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element 
twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Solution: 
Brute force approach is to check every pair can be formed using array elements.
Optimal approach is to store array element and its index in hashmap and check if target - arr[i] exists
    in hashmap if it does then return the indices of both elements.
"""

def twoSum(nums, target):
    mp = {}
    for i in range(len(nums)):
        if target - nums[i] in mp:
            return ([mp[target-nums[i]], i])
        mp[nums[i]] = i

l = list(map(int, input("Enter array elements: ").split()))
t = int(input())

print(twoSum(l, t))