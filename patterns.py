"""
Input: 5

Output:
    *
   ***  
  *****
 *******
*********
"""
def printTriangle(N):
    # Code here
    for k in range(N):
        for i in range(N-k-1):
            print(" ", end="")
        for j in range(2*k+1):
            print("*", end="")
        print()

N = int(input())
printTriangle(N)
"""
Input: 5

Output:

*********
 *******
  *****
   ***
    *
"""
def printTriangle(N):
    # Code here
    for k in range(N):
        for i in range(k):
            print(" ", end="")
        for j in range(2*(N-k)-1):
            print("*", end="")
        print()

N = int(input())
printTriangle(N)