# Import problem to break into the idea of recursion
class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
  self.val= val
  self.left= left
  self.right=right

class Solution:
  def maxDepth(self, root:Optional[treeNode]) -> int:
    if not root:
      return 0
    depth = 1
    return depth + max(self.maxDepth(root.left), self.maxDepth(root.right()))
