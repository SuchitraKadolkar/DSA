"""
Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Solution:
Brute force approach will be traverse through entire array, go element wise of store 90 degree rotation
    into another array. Time complexity is O(N2) and space complexity is O(N2)
Optimal approach is transpose a matrix then reverse each row you will get resultant matrix.
"""

def rotate(matrix):
    n = len(matrix)
    for i in range(0, n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    for row in matrix:
        row.reverse()

matrix = []
r = int(input("Enter No. of rows: "))
for i in range(r):
    l = list(map(int, input().split()))
    matrix.append(l)

rotate(matrix)
print(matrix)