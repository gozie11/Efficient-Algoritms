class MinStack:

  def __init__(self):
    """Initialize your data structures"""
    self.stack = []
    self.min_stack = []

  def push(self, val:int):
    self.stack.append(val)
    min_val = min(val, self.min_stack[-1] if self.min_stack else val)
    self.min_stack.append(min_val)
    
  def pop(self):
    self.stack.pop()
    self.min_stack.pop()

  def getMin(self) -> int:
    return self.min_stack[-1]
    
  def top(self) -> int:
    return self.stack[-1]
