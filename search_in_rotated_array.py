## this is my first attempt. It calculates mid wrong in an array of size 2. It will give you a negative index.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        result = -1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        return result
