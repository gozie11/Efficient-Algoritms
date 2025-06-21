
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

# I'm back a year later. I failed to solve this problem at a meta interview.... holy cow....
# today's attempt. passes first try.

class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        closed = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        opened = closed.values()

        for i, element in enumerate(s):
            if element in opened:
                st.append(element)
            else:
                if not st: return False
                if st[-1] == closed[element] : st.pop()
                else: return False
        
        return True if not st else False

