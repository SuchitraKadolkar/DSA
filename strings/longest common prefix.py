"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs):
    prefix = ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    if len(first) < len(last):
        length = len(first)
    else:
        length = len(last)
    for i in range(length):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix

arr = list(input("Enter words separated by spaces: ").split())
print(longestCommonPrefix(arr))