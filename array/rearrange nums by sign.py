"""
Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive 
and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do 
not satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

Solution:
Brute force approach you will separate positive and negative values into separate arrays and then
    simply place +ve elements at even indices and negative elements in odd indices.
Better approach will be initialize new array with size N and traverse through array if positive ele
    comes then place at even index otherwise place at odd index.
"""

def rearrangeArray(nums):
    """
    pos=[]
    neg=[]
    n = len(nums)
    for i in nums:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
    for i in range(n//2):
        nums[2*i] = pos[i]
        nums[2*i + 1] = neg[i]

    return nums
    """
    pos=0
    neg=1
    n = len(nums)
    output=[None]*n
    for i in nums:
        if i<0:
            output[neg] = i
            neg += 2
        else:
            output[pos] = i
            pos += 2
    
    return output

l = list(map(int, input("Enter array elements: ").split()))

print(rearrangeArray(l))