class Solution:
    def maximumCount(self, nums: List[int]) -> int:
    #The key insight is realizing that positions of transitions are often more useful than the actual values at those transitions!

        def findFirst(target_condition: Callable[[int], bool]) -> int:

            left , right = 0 , len(nums) # why don't we have to subtract 1 from len?
                                         #

            while left < right : # why not le? Bc we are using search space reduction pattern not element finding pattern
                mid = (left + right) // 2

                if target_condition(nums[mid]):
                    right = mid  #everything at right and on pass the condition   
                else:
                    left = mid + 1 # left is the last failing position 

            return left # we exit the loop when left == right to the search space is 0 and we have found our boundary
        
        
        first_positive = lambda x : x > 0
        first_non_negative = lambda x : x >= 0

        pos = len(nums) - findFirst(first_positive) #it's important to do this subtraction because 
        neg = findFirst(first_non_negative)

        return max(pos, neg)



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
