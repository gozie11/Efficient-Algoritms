class Solution:
  def diameter_of_binary_tree(root:Optional[TreeNode]) -> int:
  
    result = 0 
  
    def dfs(root:Optional[TreeNode]) -> int:
      
      nonlocal result # first memory I have using this key word. The other method is to pass it in as a parameter to the dfs call.
      
      if not root : return 0 # base case
  
      left = dfs(root.left) # It's interesting that this function within a function doesn't need to use self. to refer to itself
      right = dfs(root.right) #break down

      result = max(result , right+left) # build up
      
      return 1 + max(left, right) # build up

    dfs(root)
    return result
