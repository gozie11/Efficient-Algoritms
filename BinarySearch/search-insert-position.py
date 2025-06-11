class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Distinct so don't have to handle duplicates

        l , r = 0 , len(nums) - 1

        # there is only one element to begin with
        if r == 0 : 
            return 1 if target > nums[0] else 0

        # I got stuck on this example. stuck in infinite loop from not updating l,r correctly
        # nums =
        # [1,3,5,6]

        # targ=
        # 5
        
        while l <= r: #using <= ensures that l ends up at the actual insertion point
            # mid = (r-l) // 2 this is the wrong way to update mid... it calculates the relative distance and not absolute location!
            mid = (r+l)//2

            if target == nums[mid] : return mid # index of the found number



            # WARNING this is extra work. I tried to handle the case where there are 2 elements left, but binary search does this natively.
            # Leaving this here as a warning

            # if r - l == 1: # there are only 2 values left so pick where to put the target
            #     #mid = 1 at this point btw
            #     if target > nums[l] :
            #         if target > nums[r]: # if the target is larger than both remaining elements, put at the end
            #             return r+1
            #         return l+1 # if it's only greater than the left, put it at before right
            #     return l - 1 #less than left? put it before left

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1


        return l
