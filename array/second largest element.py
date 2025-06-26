"""
Second Largest Element in an Array

Given an array of positive integers arr[] of size n, the task is to find second largest distinct element 
in the array.
Note: If the second largest element does not exist, return -1.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.


Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.


Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 there is no second largest element.

"""

"""
Solution: Use 2 variables to keep track of largest and second largest element.

Time Complexity: O(n)
Space Complexity: O(1)

"""

def second_largest(arr):
    largest = -1
    second_largest = -1

    if len(arr) < 2:
        return -1

    for ele in arr:
        if ele > largest:
            second_largest = largest
            largest = ele
        elif ele > second_largest and ele != largest:
            second_largest = ele

    return second_largest

arr = list(map(int, input("Enter int array elements: ").split()))

print(second_largest(arr))