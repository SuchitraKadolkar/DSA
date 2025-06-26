"""
Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts 
on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false

Solution:
length of both strings should be same and check if goal is present in string s+s (i.e abcdeabcde)
"""

def rotateString(s, goal):
    if len(s) == len(goal) and goal in s+s:
        return True
    else:
        return False
    
s = input("Enter first string: ")
goal = input("Enter target string: ")

print(rotateString(s, goal))