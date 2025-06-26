"""
Maximum Nesting Depth of the Parentheses
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum 
number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3

"""

def maxDepth(s):
    maxDepth = 0
    depth = 0
    for char in s:
        if char == "(":
            depth += 1
            maxDepth = max(maxDepth, depth)
        elif char == ")":
            depth -= 1
        
    return maxDepth

s = input("Enter balanced parenthesis string: ")
print(maxDepth(s))