class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #time: O(N)
        #space:O(N)
        location = {}
        for i in range(len(nums)):
            if target-nums[i] in location:
                return [i, location.get(target-nums[i])]
            else:
                location[nums[i]]=i
