class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #get the depth of the left and right subtrees at each node and compare.

        def dfs(root):
            if not root: return[True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and (abs(left[1]-right[1]) <= 1)

            return(balanced, 1 + max(left[1],right[1]))

        return dfs(root)[0]

        
