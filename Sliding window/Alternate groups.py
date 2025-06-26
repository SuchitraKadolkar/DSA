"""
Alternating Groups II
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. 
The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in 
the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to 
each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

"""
def numberOfAlternatingGroups(colors, k):
    n = len(colors)
    result = 0
    alternate_seq = 1
    last_color = colors[0]

    for i in range(1, n + k -1):
        index = i % n
        print(i, result, alternate_seq)
        if colors[index] == last_color:
            alternate_seq = 1
            continue
        
        alternate_seq += 1
        if alternate_seq >= k:
            result += 1
        
        last_color = colors[index]
    return result

arr = [int(x) for x in input("Enter array elements: ").split()]
k = int(input())
print(numberOfAlternatingGroups(arr, k))

d = {}

keys = dict(sorted(d.items()))
val = dict(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))
max_key, min_key = max(d), min(d)
max_val, min_val = max(d, key=d.get), min(d, key=d.get)