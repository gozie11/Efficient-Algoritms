class Solution:
    def maximumCount(self, nums: List[int]) -> int:
    #The key insight is realizing that positions of transitions are often more useful than the actual values at those transitions!

        def findFirst(target_condition):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if target_condition(nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        first_non_neg = findFirst(lambda x: x >= 0)
        first_pos = findFirst(lambda x: x > 0)
        
        neg_count = first_non_neg
        pos_count = len(nums) - first_pos
        
        return max(neg_count, pos_count)


        # My first working binary search attempt is brutish so I will learn the above approach
        # left = 0
        # right = len(nums)-1
        # while left <= right : # find first negative number
        #     mid = (right + left) // 2

        #     if nums[mid] < 0:
        #         if mid+1 < len(nums) and nums[mid+1] < 0 :
        #             left = mid + 1
        #         else:
        #             neg = mid + 1 # add one because 0 indexed
        #             # All elements from 0 to mid are negative
        #             break # MY INTUITION WAS RIGHT
        #     else:
        #         right = mid - 1

        # left = 0
        # right = len(nums)-1
        # while left <= right : # find first positive number
        #     mid = (right + left) // 2

        #     if nums[mid] > 0:
        #         if mid-1 >= 0 and nums[mid-1] > 0 :
        #             right = mid - 1
        #         else:
        #             pos = len(nums) - mid # All elements from mid to end are positive
        #             break # MY INTUITION WAS RIGHT

        #     else: 
        #         left = mid + 1


        
        # return max(pos,neg)
