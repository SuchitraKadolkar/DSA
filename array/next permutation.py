"""
Given an array arr[] of size n, the task is to print the lexicographically next greater permutation of 
the given array. If there does not exist any greater permutation, then find the lexicographically 
smallest permutation of the given array.

Let us understand the problem better by writing all permutations of [1, 2, 4] in lexicographical order

[1, 2, 4], [1, 4, 2], [2, 1, 4], [2, 4, 1], [4, 1, 2] and [4, 2, 1]

If we give any of the above (except the last) as input, we need to find the next one in sequence. If 
we give last as input, we need to return the first one.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is 2 4 5 0 1 7


Input: arr = {3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation. So, the next permutation is the lowest one.
"""

"""
Solution:
Let’s try some examples to see if we can recognize some patterns. 

[1, 2, 3, 4, 5]: next is [1, 2, 3, 5, 4]  
Observation: 4 moves and 5 comes in place of it


[1, 2, 3, 5, 4]: next is [1, 2, 4, 3, 5] 
Observation: 3 moves, 4 comes in place of it. 3 comes before 5 (mainly 3 and 5 are in sorted order)


[1, 2, 3, 6, 5, 4]: next is [1, 2, 4, 3, 5, 6] 
Observation: 3 moves, 4 comes in place of it. [3, 5 and 6 are placed in sorted order]


[3, 2, 1]: next is [1, 2, 3]
Observation: All elements are reverse sorted. Result is whole array sorted.


[1, 2, 3, 6, 4, 5]: next is [1, 2, 3, 6, 5, 4] 
Observation: 4 moves and 5 comes in place of it


Observations of Next permutation: 

To get the next permutation we change the number in a position which is as right as possible.
The first number to be moved is the rightmost number smaller than its next.
The number to come in-place is the rightmost greater number on right side of the pivot.
Each permutation (except the very first) has an increasing suffix. Now if we change the pattern from 
the pivot point (where the increasing suffix breaks)
to its next possible lexicographic representation we will get the next greater permutation.
"""

def next_permutation(arr):
    n = len(arr)
    pivot = -1

    for i in range(n-2, -1 , -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    if pivot == -1:
        arr.reverse()
        return arr
    
    for i in range(n-1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    left, right = pivot+1, n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

arr = list(map(int, input("Enter array elements: ").split(" ")))

print(next_permutation(arr))