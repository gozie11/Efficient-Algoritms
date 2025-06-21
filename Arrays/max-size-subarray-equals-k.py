class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest_subarray = 0

        indices = {0 : -1} # why is this useful again? this allows you to omit if prefix_sum == k: longest_subarray = i + 1. why?

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                longest_subarray = i + 1
            
            if (prefix_sum - k) in indices: # we found our complementary subarray
                # a subarray with sum k will be missed
                longest_subarray = max(longest_subarray, i-indices[prefix_sum - k]) #very cool logic wow

            if prefix_sum not in indices:
                indices[prefix_sum] = i
        return longest_subarray
