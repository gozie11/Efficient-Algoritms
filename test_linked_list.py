import unittest
from random_pointer_linked_list import Node, print_list, copyRandomList

class TestLinkedList(unittest.TestCase):

    def test_deep_copy(self):
        # Create original linked list
        head = Node(7)
        head.next = Node(13)
        head.next.next = Node(11)   
        head.next.next.next = Node(10)
        head.next.next.next.next = Node(1)
        head.random = None
        head.next.random = head
        head.next.next.random = head.next.next.next.next
        head.next.next.next.random = head.next.next
        head.next.next.next.next.random = head

        # Create deep copy
        print_list(head)
        new_head = copyRandomList(head)

        # Validate deep copy
        original = head
        copied = new_head

        while original and copied:
            self.assertEqual(original.val, copied.val)
            self.assertEqual(original.random.val if original.random else None, copied.random.val if copied.random else None)
            original = original.next
            copied = copied.next

if __name__ == '__main__':
    unittest.main()
