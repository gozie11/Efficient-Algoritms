#What's the minimum number of bananas koko can eat per hour before the guards come back?

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h: #if we did this in the right mount of time
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


