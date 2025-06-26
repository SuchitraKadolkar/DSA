"""
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum 
equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Solution:
Optimal approach: You have a prefixSum s which is the entire sum at particular index and you are looking
    for k and you just look for how many times (s-k) appeared and that will be the number of subarrays
    which ends at that particular index
"""

def subarraySum(nums, k):
    prefixSum = 0
    mp = {}
    cnt = 0
    for i in range(len(nums)):
        prefixSum += nums[i]
        if prefixSum == k:
            cnt += 1
        if (prefixSum - k) in mp:
            cnt += mp[prefixSum-k]
        if prefixSum in mp:
            mp[prefixSum] += 1
        else:
            mp[prefixSum] = 1
        print(mp)
    return cnt

l = [int(x) for x in input("Enter array elements: ").split()]
k = int(input("Enter k Value: "))

print(subarraySum(l, k))