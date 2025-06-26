"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(s):
    maxCnt = 0
    left, right = 0, 0
    mp = {}
    while right < len(s):
        if s[right] in mp:
            if mp[s[right]] >= left:
                left = mp[s[right]] + 1
        
        maxCnt = max(maxCnt, right-left+1)
        mp[s[right]] = right
        right += 1
    return maxCnt

s = input("Enter String: ")
print(lengthOfLongestSubstring(s))