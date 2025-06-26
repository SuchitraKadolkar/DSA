"""
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d 
positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, 
arr[] becomes {3, 4, 5, 6, 1, 2}


Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
Explanation: The array is rotated as follows:


After first left rotation, arr[] = {2, 3, 1}
After second left rotation, arr[] = {3, 1, 2}
After third left rotation, arr[] = {1, 2, 3}
After fourth left rotation, arr[] = {2, 3, 1}
"""

"""
Solution: 

The idea is based on the observation that if we left rotate the array by d positions, 
the last (n - d) elements will be at the front and the first d elements will be at the end. 
Reverse the subarray containing the first d elements of the array.
Reverse the subarray containing the last (n - d) elements of the array.
Finally, reverse all the elements of the array.
"""

def left_rotate_arr(arr, d):
    n = len(arr)
    d %= n
    reverse(arr, 0, d-1)

    reverse(arr, d, n-1)

    reverse(arr, 0, n-1)

def right_rotate_arr(arr, d):
    n = len(arr)
    d %= n

    reverse(arr, 0, n-1)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)

def reverse(arr, startindex, endindex):
    while startindex < endindex:
        arr[startindex], arr[endindex] = arr[endindex], arr[startindex]
        startindex += 1
        endindex -= 1

arr = list(map(int, input("Enter array elements: ").split(" ")))
temp = arr
d = int(input("Enter d value to left shift all array elements: "))

left_rotate_arr(arr, d)
print(arr)
right_rotate_arr(temp, d)
print(arr)


