"""
Check if a string is substring of another
Given two strings txt and pat, the task is to find if pat is a substring of txt. If yes, return the 
index of the first occurrence, else return -1.

Examples : 

Input: txt = “geeksforgeeks”, pat = “eks”
Output: 2
Explanation: String “eks” is present at index 2 and 9, so 2 is the smallest index.


Input: txt = “geeksforgeeks”, pat = “xyz”
Output: -1.
Explanation: There is no occurrence of “xyz” in “geeksforgeeks”
"""

# Python program to check if a string is a substring of another
# using nested loops

# Function to find if pat is a substring of txt
def findSubstring(txt, pat):
    n = len(txt)
    m = len(pat)

    # Iterate through txt
    for i in range(n - m + 1):

        # Check for substring match
        j = 0
        while j < m and txt[i + j] == pat[j]:
            j += 1
        
        # If we completed the inner loop, we found a match
        if j == m:
            return i

    # No match found
    return -1

if __name__ == "__main__":
    txt = "geeksforgeeks"
    pat = "eks"
    print(findSubstring(txt, pat))
