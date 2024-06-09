
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:
    def is_valid(self, s:str) -> bool:
        s = "([)]"
        complements = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in complements: # complements here will only reference the keys of the dictionary!
                if not stack or stack[-1] != complements[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack


complements = {')': '(', ']': '[', '}': '{'}


#06/09/24 ... My skills worsened after 2 months off.

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2: return False

        dic = {")":"(",
                "}":"{",
                "]":"["
                }

        stack = []

        for let in s:
            if let in dic.values():
                stack.append(let)
            if let in dic.keys():
                if not stack or stack[-1] != dic[let]: return False
                else: stack.pop()
        return False if stack else True


