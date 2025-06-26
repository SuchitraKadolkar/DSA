"""
Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc",
 "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb",
"aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
"""

def numberOfSubstrings(s):
    left, right = 0, 0
    mp ={}
    count = 0
    n = len(s)
    while right < n:
        mp[s[right]] = mp.get(s[right], 0) + 1
        while len(mp) == 3:
            count += n - right
            if mp[s[left]] == 1:
                del mp[s[left]]
            else:
                mp[s[left]] -= 1
            left += 1
        right += 1
    return count

s = input("Enter string containing chars a,b and c: ")
print(numberOfSubstrings(s))