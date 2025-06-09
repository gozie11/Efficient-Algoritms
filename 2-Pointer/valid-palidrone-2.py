class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s,l,r):
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

        l , r = 0 , len(s)-1

        while l<r:
            if s[l]!= s[r]:
                if isPalindrome(s,l+1,r) or isPalindrome(s, l, r-1):
                    return True

                else:
                    return False

            r-=1
            l+=1
        return True