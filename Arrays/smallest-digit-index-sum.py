# Leetcode 3550
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def get_num_sum(number:int) -> int:
            return sum(int(let) for let in str(number))
        
        i = 0 
        while i < len(nums):
            isum = get_num_sum(nums[i])
            if i == isum : return i
            i += 1
        return -1
