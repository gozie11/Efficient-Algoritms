class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset =[]
        def dfs(i):
            #base case
            if i >= len(nums):
                #It's important to use the copy method here because list are accessed by reference. 
                #This means that all the list we append to result will be modified in subsequent recursive calls if we don't 
                #ensure a coppy is appended to the answer instead of the original.
                res.append(subset.copy())
                return
            #left of decision tree
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
            return
        
        dfs(0)
    
        return res
