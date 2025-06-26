"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in 
place such that each unique element appears only once. The relative order of the elements should be 
kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should 
hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array

Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in 
 the beginning of the array.

Example 2:
Input:
 arr[1,1,1,2,2,3,3,3,3,4,4]

Output:
 arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation:
 Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] 
 in the beginning of the array.
"""

def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1
    
    
if __name__ == '__main__':
    arr = [1,1,2,2,3,4,5,6,6]
    k = removeDuplicates(arr)
    print(arr)

"""
Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the 
result be placed in the first part of the array nums. More formally, if there are k elements after 
removing the duplicates, then the first k elements of nums should hold the final result. It does not 
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 
and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 
1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def removeDuplicates(nums):
    left = right = 0
    n = len(nums)
    while right < n:
        count = 1
        while right + 1 < n and nums[right] == nums[right+1]:
            right += 1
            count += 1
        for i in range(min(2,count)):
            nums[left] = nums[right]
            left += 1
        right += 1
    return left

arr = [int(x) for x in input("Enterarray elements: ").split()]
index = removeDuplicates(arr)
print(arr[:index])

"""
Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in 
the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
def containsNearbyDuplicate(nums, k):
    mp = {}
    
    for i, num in enumerate(nums):
        if num in mp and (i - mp[num]) <= k:
            return True
        mp[num] = i
    return False

nums = [int(x) for x in input("Enter array elements: ").split()]
print(containsNearbyDuplicate(nums))