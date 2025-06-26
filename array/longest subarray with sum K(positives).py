"""
 Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Examples
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""

def logestSubArrCnt(arr, k):
    i, j = 0, 0
    Sum = arr[0]
    max_len = 0
    n = len(arr)
    while j < n:
        while i <= j and Sum > k:
            Sum = Sum - arr[i]
            i += 1
        if Sum == k:
            max_len = max(max_len, j-i+1)
        j += 1
        if j < n:
            Sum += arr[j]

    return max_len

l = list(map(int, input("Enter array elements: ").split(" ")))
k = int(input())

print(logestSubArrCnt(l, k))
