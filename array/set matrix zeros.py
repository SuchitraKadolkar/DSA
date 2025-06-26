"""
Set Matrix Zeroes
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Solution:
Brute force approach is to traverse through array if zero element occurs you replace every other 
    element in that particular col and row with -1. After this complete loop(n*m), we again traverse
    through array and replace -1 with 0 to get resultant output. Time complexity will be O(N3)
Optimal will be initialize row and col arrays with 0 and traverse through array when you find 0 element,
    set row[i] and col[j] to 1. Then, traverse through matrix if row[i] or col[j] is set 1 we have to
    make that element is 0 and so on. 
"""

def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = [None]*n
    col = [None]*m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

matrix = []
r = int(input("Enter No. of rows: "))
print("Enter array elements row by row: ")
for i in range(r):
    l = list(map(int, input().split()))
    matrix.append(l)

setZeroes(matrix)
print(matrix)