# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
# Easy
# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            left = s[i-1] if i > 0 else ''
            right = s[i+1] if i < len(s)-1 else ''
            if s[i] == '?':
                for c in 'abc':
                    if c != left and c != right:
                        s[i] = c
                        break
        return ''.join(s)
        
# class Solution:
#     def modifyString(self, s: str) -> str:

#         # first thought was sliding window but ERR
#         # Seems to be a greedy algorithm ie you can find the best solution at each step of the problem?

#         s = list(s)
#         for i in range(len(s)):
#             if s[i] == '?': #what do we want to do if we hit a question mark
#                 for  c in "abc": # 3 choices are enough to avoid neighbors
#                     if (i == 0 or c != s[i-1]) and (i == len(s)-1 or c != s[i+1]):
#                         #1st case... if the first letter is a ?, and the following letter is not abc, set it to abc
#                         #2nd case... if we are onto the next letter,  and neither the prior or the following letter is == to the current abc,
#                             # set the question mark at i to the current ab or c.
#                         #3rd case... we're on a question mark & it is the first or last letter in the string, set it to a valid ab or c.
#                         s[i] = c
#                         break
#         return ''.join(s)
