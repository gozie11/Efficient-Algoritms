#Wooo got this one on my own. Relatively straight forward in order traversal of a bst.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        in_order = []

        def dfs(root):

            if not root: return

            dfs(root.left)
            in_order.append(root.val)
            dfs(root.right)

        dfs(root)

        print(in_order)

        return in_order[k-1]
