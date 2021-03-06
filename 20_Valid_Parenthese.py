# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

# https://leetcode.com/problems/valid-parentheses/description/

# 1) use dict and stack (list) right:left as key-value pair, O(N) time complexity
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parent_dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char not in parent_dict:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                elif parent_dict[char]!= stack.pop(): return False

        return True if len(stack) == 0 else False

# 2) cleaner version of 1)
class Solution(object):
    def isValid(self, s):
        stack, paren_map = [], {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in paren_map: stack.append(c)
            elif not stack or paren_map[c] != stack.pop(): return False
        return not stack

# 3) use set and stack (list)
class Solution(object):
    def isValid(self, s):

        if len(s)%2!=0:
            return False
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack)==0:
                    return False
                if (stack.pop(), paren) not in  matches:
                    return False
        return len(stack)==0
