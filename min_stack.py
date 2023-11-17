class MinStack:

  def __init__(self):
    """Initialize your data structures"""
    stack = []
    min_stack = []

  def push(self, val:int):
    stack.append(val)
    min_val = min(val, min_stack[-1] if min_stack else val)
    min_stack.append(min_stack)
    
  def pop(self):
    stack.pop()
    min_stack.pop()

  def getMin(self) -> int:
    return min_stack[-1]
    
  def top(self) -> int:
    return stack[-1]
