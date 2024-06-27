# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
U: 
    is there at least one node
    return boolean
    sy : if there's a node pointing to null, there's no cycle

M:
    Fast pointer slow pointer

P:
    slow = head
    fast = head.next

    if fast == None: return False

    while fast != None : keep checking next nodes 

        check if pointers are equal to each other

        increment pointers

    return False

I:

Review:

E:
time O(n) . n = number of nodes
space O(1)

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        
        if head.next:
            fast = head.next
        else:
            return False

        while fast:
            if slow == fast: return True

            else:
                slow = slow.next
                if fast.next: # important not to check fast.next.next here becasue fast.next could be null
                    fast = fast.next.next
                else:
                    return False

        return False
