"""
Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects 
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Solution:
Brute force approach is to use any sorting algorithm which will take nlogn in worst case
better approach is to count 0,1 and 2 in an array and simply overwrite the number of 0's, 1's and
    2's in the array. It will take O(2*N) time complexity.
optimal solution is to use 3 pointers low, mid, high which will follow below rules.
    1. 0 - (low-1) = sorted contains all 0's
    2. low - (mid-1) = sorted contains all 1's
    3. mid - high = unsorted (our task is to sort)
    4. (high+1) - (n-1) = sorted containes all 2's

    Time complexity for this approach is O(N) and space complexity is O(1)


"""
def sortColors(nums):
    """
    Better Approach:

    cnt_0, cnt_1, cnt_2 = 0, 0, 0

    for i in nums:
        if i == 0:
            cnt_0 += 1
        elif i == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1
    
    i = 0
    while(cnt_0):
        nums[i] = 0
        i += 1
        cnt_0 -=1
    while(cnt_1):
        nums[i] = 1
        i += 1
        cnt_1 -=1 
    while(cnt_2):
        nums[i] = 2
        i+= 1
        cnt_2 -= 1

    """
    """
    Dutch national flag algorithm
    """
    low, mid = 0, 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
l = list(map(int, input("Enter array elements: ").split()))

sortColors(l)
print(l)