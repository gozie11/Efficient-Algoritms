class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0

        if not s: return 0
        if len(s) < 2 : return 1

        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set: # I need to understand this chunk a bit better.
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, (r - l)+1)
        return longest
