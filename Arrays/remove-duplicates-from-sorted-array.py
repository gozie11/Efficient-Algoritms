class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [ 0 1 0 1] -> [0 1 - - -]

        # deepseek just showed me that I don't need a hash map
        # learned hashmaps can also lead to degraded performance if there are memory collisions etc.
        # 
        if not nums: return 0
        i = k = 1
        while i < len(nums):
            if nums[i-1] != nums[i]: # found a unique number
                nums[k] = nums[i]
                k+=1
            i+=1
        return k


    #Working solution using hash maps
        # found = {} # using a set here as well as an add function on line 8 make the runtime tripple.
        # i = k = 0 
        # while i < len(nums):
        #     if not (nums[i] in found):
        #         found[nums[i]] = 1
        #         nums[k] = nums[i]
        #         k+=1
        #     i+=1
        # return k

#   For loop version of the problem . Seems to take 1 ms longer than the while. 
        # for i in range(len(nums)):
        #     if nums[i] not in found:
        #         found[nums[i]] = 1
        #         nums[k] = nums[i]
        #         k+=1

       
        # return k
