""" 
Humble brag... I solved this in 6 minutes from the first time I read it :)
Glad to see progress. You can do it.

^not sure when that was... 03/03 I took a bit longer solving the problem. we're hooman.

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # I want to swap the children of each node

        #base case: we have no nodes
        #break down: swap the nodes using temp values . call the function on the left and right children
        #build up: set the left node = to a recursive call of the function and do the same for the right

        if root == None:
            return None
        
        temp_left = root.left 
        temp_right = root.right 

        root.left = temp_right
        root.right = temp_left
        
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
