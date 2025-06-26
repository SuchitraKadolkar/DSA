"""
Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

Solution:
Brute force approach is to check for every element ele + 1 exists in array and if exists then increase
    the count then check for ele + 2 and so on. The movement you don't find ele + 1 in array you stop
    iterating and goto second element and do the same process. Time complexity for this is O(N2)
Better approach is to sort array and then select element from array and check if next ele is currEle + 1
    if it does increase count and go for next index and so on. It will not iterate for another ele to 
    find max count.
Optimal approach is to use set and iterate over set, check if ele - 1 exists then you skip the searching
    for ele + 1 and go for next element. If ele - 1 doesnot exists then you will search for ele + 1, 
    ele + 2, and so on and increase the count according. Time complexity is O(2N) ~= O(N)
"""

def longestConsecutive(nums):
    n = len(nums)
    set_n = set(nums)
    currMax = 0
    for ele in set_n:
        if ele - 1 not in set_n:
            i = 1
            cnt = 1
            while True:
                if ele + i in set_n:
                    cnt += 1
                    i += 1
                else:
                    currMax = max(currMax, cnt)
                    break
    return currMax

l = list(map(int, input("Enter array elements: ").split()))

print(longestConsecutive(l))