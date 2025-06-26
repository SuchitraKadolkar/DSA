"""
Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses 
strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it 
into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where 
Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive 
decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""
def removeOuterParenthesis(s):
    cnt = 0
    output = ""

    for char in s:
        if char == "(":
            if cnt != 0:
                output += char
            cnt += 1
        else:
            cnt -= 1
            if cnt != 0:
                output += char

    return output

s = input("Enter valid string: ")
print(removeOuterParenthesis(s))

"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""

def isValid(self, s: str) -> bool:
    opened = ["(", "[", "{"]

    arr = []
    for char in s:
        if char in opened:
            arr.append(char)
        else:
            if char == ")":
                if arr and arr[-1] == "(":
                    arr.pop(-1)
                else:
                    return False
            elif char == "]":
                if arr and arr[-1] == '[':
                    arr.pop(-1)
                else:
                    return False
            else:
                if arr and arr[-1] == '{':
                    arr.pop(-1)
                else:
                    return False
    if arr:
        return False
    return True