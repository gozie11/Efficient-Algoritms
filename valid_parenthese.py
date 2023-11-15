
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:


    def is_valid(self, s:str) -> bool:
        s = "([)]"
        complements = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in complements:
                if not stack or stack[-1] != complements[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack