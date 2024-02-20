class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset =[]
        def dfs(i):
            #base case
            if i >= len(nums):
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
