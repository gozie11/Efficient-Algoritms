""" 
Humble brag... I solved this in 6 minutes from the first time I read it :)
Glad to see progress. You can do it.

"""
Class Solution:
  def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
    if not root : return None
  
    temp_left = root.left
    temp_right = root.right
  
    root.left = temp_right
    root.right = temp_left
  
    self.invertTree(root.left)
    self.invertTree(root.rigth)

    return root
