"""
Move all zeros to end of array

Given an array of integers arr[], the task is to move all the zeros to the end of the array while 
maintaining the relative order of all non-zero elements.

Examples: 

i , j = 0, 0
for k in range(len(l)):
    if arr[k] == 0:
        
    else:
        i += 1
    j += 1


Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.


Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s.

"""

"""
Solution: Traverse through arr with 2 variables, i and count, when we encounter zero then 
we simply increment i variable until we find next non-zero element.
When we found next non-zero element then swap i and count and increment count variable. 

Time Complexity: O(n)
Space Complexity: O(1)

"""

def move_zeros_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr

arr = list(map(int, input("Enter array elements: ").split(" ")))

print(move_zeros_to_end(arr))

