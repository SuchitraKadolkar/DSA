"""
Minimum Recolors to Get K Consecutive Black Blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', 
representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, 
respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k 
consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Solution:
Optimal approach: Since existing black blocks don't require recolors, our required number of operations
    is determined by the number of white blocks within each segment of k consecutive blocks. The fewer 
    white blocks in a segment, the fewer recolors we need. This immediately tells us that our task is 
    to identify the segment of k consecutive blocks that contains the fewest white blocks.
"""

def minimumRecolors(blocks, k):
    i = 0
    minWhite = 1e6
    n = len(blocks)
    while (i + k) <= n:
        cnt = blocks[i:(i+k)].count('W')
        minWhite = min(cnt, minWhite)
        i+=1
    return minWhite 

s = input("Enter String: ")
k = int(input("Enter K value: "))
print(minimumRecolors(s, k))