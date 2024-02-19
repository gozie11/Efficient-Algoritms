def isSubTree(self, root:Optional[TreeNode], subTree: Option[TreeNode])-> bool:
  if not subTree: return True #An emptry tree is a subtree of any tree
  if not root: rutrn False #An emptry tree is not the main tree of any subroot. Get it? ask in the issues for a clearer explanation if necessary

  if sameTree(root, subTree): return True 

  # recursively call this function to chekc the children of the original tree against the subtree. Get it?
  return(
    self.isSubTree(root.left, subTree) 
    or
    self.isSubTree(root.right, subTree) 
  )


def sameTree(self, s: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
  #two empty trees are the same tree
  if not s and not r: return True

  # build up recursively if both trees exist
  if s and r and s.val == r.val:
    return(self.sameTree(s.left, r.left) and
          self.sameTrre(s.right, r.right))

  return False
