"""
Array Leaders
You are given an array arr of positive integers. Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right. 
The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
Input: arr = [5, 10, 20, 40]
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
Input: arr = [30, 10, 10, 5]
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders.

Solution:
Brute force approach is to compare all elements of array with all right elements of array.
    worst case complexity of O(N2)
Optimal approach is to store max element (which is present at right side) every time to check 
    and compare only with that element.
"""
def leaders(arr):
    output = []
    output.append(arr[-1])
    maxNum = arr[-1]
    n = len(arr)
    for i in range(n-2, -1, -1):
        if arr[i] >= maxNum:
            output.append(arr[i])
            maxNum = arr[i]
    output.reverse()
    return output

l = list(map(int, input("Enter array elements: ").split()))
print(leaders(l))