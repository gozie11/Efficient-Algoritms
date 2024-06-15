class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if s1 is larger than s2
        if len(s1) > len(s2):
            return False
        
        # Create frequency maps for s1 and the initial window in s2
        map1 = {}
        map2 = {}
        
        for let in s1:
            map1[let] = map1.get(let, 0) + 1
        
        for let in s2[:len(s1)]: #ALERT! You are only initializing the length of s1 worth of s2!..
            map2[let] = map2.get(let, 0) + 1
        
        # Use a sliding window to compare frequencies
        l = 0
        for r in range(len(s1), len(s2)):
            if map1 == map2:
                return True
            
            # Add the new character to the window
            map2[s2[r]] = map2.get(s2[r], 0) + 1
            
            # Remove the old character from the window
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                del map2[s2[l]]
            
            l += 1
        
        # Check the last window
        return map1 == map2

# Example usage:
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # Should return True
print(sol.checkInclusion("ab", "eidboaoo"))  # Should return False
