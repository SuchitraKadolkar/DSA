"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

def longestPalindrome(self, s: str) -> str:
    res = ""
    resLen = 0
    length = len(s)
    for i in range(length): 
        # odd length
        l, r = i, i
        while l >= 0 and r < length and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1
        # even length
        l, r = i-1, i
        while l >= 0 and r < length and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1
    return res

s = input("Enter string: ")
print(longestPalindrome(s))