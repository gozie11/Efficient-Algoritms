class Node:
  def __init__(self, val:int):
      self.val = val
      self.left = None
      self.right = None


def bfs(root:Node) -> None:
  if not root: return None

  queue = []

  queue.append(root)

  while queue:
    print(queue[0] , end=" ") 

    node = queue.pop(0) # important to pop index 0 because that is how a queue operates. the first element in is the first element out!

    if node.left : queue.append(node.left)
    if node.right : queue.append(node.right)

    
    
