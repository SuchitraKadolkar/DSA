"""
Union of 2 Sorted with Duplicates
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to 
return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in 
either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.
"""

def findUnion(a, b):
    """
    Without using set approach:
    
    i, j = 0, 0
    output = []
    lastele = -1
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ele = a[i]
            i += 1
        else:
            ele = b[j]
            j += 1
        if ele > lastele:
            output.append(ele)
            lastele = ele

    while i < len(a):
        if a[i] > lastele:
            output.append(a[i])
            lastele = a[i]
            i += 1

    while j < len(b):
        if b[j] > lastele:
            output.append(b[j])
            lastele = b[j]
            j += 1
    return output
    """
    set_a = set(a)
    set_b = set(b)
    union_set = set_a.union(set_b)
    l = list(union_set)
    l.sort()
    return l

arr1 = list(map(int, input("Enter array 1 elements: ").split()))
arr2 = list(map(int, input("Enter array 2 elements: ").split()))

print(findUnion(arr1, arr2))