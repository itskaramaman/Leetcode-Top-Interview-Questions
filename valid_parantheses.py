Valid Parantheses https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

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
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

# Solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d={'}':'{', ')':'(', ']':'['}
        for i in s:
            if i in d.keys() and len(stack)==0:
                return False
            if i not in d.keys():
                stack.append(i)
            if i in d.keys():
                if stack[-1] != d[i]:
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0
        
