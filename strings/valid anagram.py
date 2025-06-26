"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""
from collections import Counter
def validAnagram(s, t):

    """
    Another way is by using Counter

    return Counter(s) == Counter(t)   
    """
    if len(s) == len(t):
        s = sorted(list(s))
        t = sorted(list(t))

        if s == t:
            return True
        return False
    return False

s = input("Enter string1: ")
t = input("Enter string2: ")

print(validAnagram(s, t))