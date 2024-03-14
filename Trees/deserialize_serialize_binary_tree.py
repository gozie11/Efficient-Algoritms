class Solution():
  '''
  this problem shows how to convert a binary tree to serialized form which can make it easier to transfer/write to other formats.
  The method to deserialize is given as well
  '''
  def serialize(self, root) :
    nodes = [] # the 

    def dfs(node):
      if not node:
        return "N"
      #preorder addition of nodes to our list
      nodes.append(string(node.value))
      dfs(node.left) # I need to draw a picture that shows the nodes getting added to the list cause I'm confused
      dfs(node.righ)
      
    dfs(root)
    return nodes.join(",")

  def deserialize(self, data):
    nodes = data.split(",")
    self.i=0 # this is going to be used to track which node we are looking at in our serialized tree

    def dfs() :
      if nodes[self.i] == "N"
        self.i += 1
        return None 
      new_tree = TreeNode(int(nodes[self.i]))
      self.i += 1
      new_tree.left = dfs()
      new_tree.right = dfs()
      return new_tree
      
    return dfs()


    
