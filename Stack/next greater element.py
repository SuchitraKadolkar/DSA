"""
Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right
of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next 
greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this 
query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described 
above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
Solution: 
Time complexity is O(2N) and Space complexity is also O(2N)
"""

def nextGreaterElement(nums1, nums2):
    stack = []
    n = len(nums2)
    nge = {}
    for i in range(n-1, -1, -1):
        found = False
        while stack:
            if stack[-1] > nums2[i]:
                nge[nums2[i]] = stack[-1]
                stack.append(nums2[i])
                found = True
                break
            else:
                stack.pop(-1)
        if not found:
            nge[nums2[i]] = -1
            stack.append(nums2[i])
    
    output = []

    for ele in nums1:
        output.append(nge[ele])

    return output

arr1 = [int(x) for x in input("Enter array elements: ").split()]
arr2 = [int(x) for x in input("Enter subarray elements: ").split()]

print(nextGreaterElement(arr2, arr1))