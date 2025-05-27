class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # I initially thought this was greedy because we want to tknow the 
        # the closest heater for each house. However this is not correct because
        # what we actually want is the global minima. this leads us towards 
        # a binary search approach.
        # once the heaters and houses are sorted, we can disregard one half of the 
        # heaters and focus on narrowing down our search space for the smallest radius

        # first accepted submission ~ 05/26/25 11:30pm
        
        houses.sort()
        heaters.sort()
        def is_possible(R):
            i = 0 # heater pointer
            for house in houses:
                while i < len(heaters) and heaters[i] + R < house: # this is necessarry to locate the first house and a heater that can cover the radius of the current house
                    i += 1
                if i == len(heaters) or house < heaters[i] - R: # the len of heaters is out of bounds. or is the distance covered by the radius R unable to reach the current house
                    return False
            return True
                

        left, right = 0, max(max(houses),max(heaters))
        while left < right:
            mid = (left + right) // 2 # double slash for integer division
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left# how do we know we can just return here? 
