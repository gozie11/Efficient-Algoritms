class ListNode(self, int:data, ListNode:next):
  self.data = data
  self.next = next
def reverseKnodes (self, head, k):
  dummy = ListNode(0,head)
  prev_group = dummy

  while True:
    kth = self.getKthNode(prev_group.next, k)
    if not kth : break

    next_group = kth.next
    #reverse the current group
    curr, prev = prev_group.next, kth.next
    while curr != next_group: # next group is the boundary of the reversals
      temp = curr.next
      curr.next = prev # reverse the pointer of the current node!
      prev = curr
      curr = temp
    temp = prev_group.next
    prev_group.next = kth
    prev_group = temp
  return dummy.next

    #update the prev_group pointer

def getKthNode (self, curr, k):
  while K > 0 and curr:
    curr = curr.next
    k -= 1
  return curr
