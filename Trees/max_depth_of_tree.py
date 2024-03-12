# Important problem to break into the idea of recursion
class Solution:
  def maxDepth(self, root:Optional[treeNode]) -> int:
    if not root:
      return 0
    depth = 1
    return depth + max(self.maxDepth(root.left), self.maxDepth(root.right()))

  # I came up with this solution in 13 minutes. Should've taken 5 since I've seen this.
  # Initially I thought that I would need a helper function so started building it.
  # That might show that I didn't fully understand the question.
  # Understanding that ADDING the height of the current node (1) to the next recursive call is the most important
  # thing for me to hold on to. It is how the recursion gets built up!
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Base case : No node
    # Break down : check the depth of both children
    # build up : ADD the current node node height to 
    # max (of the call on the subsequent recursive calls of left and right children)

    if not root: return 0

    left = 1 + self.maxDepth(root.left)
    right = 1 + self.maxDepth(root.right)

    return max(left,right)
