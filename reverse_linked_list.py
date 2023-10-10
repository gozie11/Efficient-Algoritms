class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next

def print_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def main():

    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = None


    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    print_list(prev)
    return prev

if __name__ == "__main__":
    main()