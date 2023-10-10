#Creatin a deep comy of a linked list with random pointers
# Writing this code was much easier thanks to the help of github copilot

# TODO (Gozie): figure out how to feed input to main and test the code
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def print_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def main():     
    
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    new_to_old = {None: None}
    print_list(head)
    currernt = head
    while current:
        new_to_old[current] = Node(current.val)
        print_list(new_to_old[current])
        current = current.next


    current = head

    while current:
        new_to_old[current].next = new_to_old[current.next]
        new_to_old[current].random = new_to_old[current.random]
        print_list(new_to_old[current])
        current = current.next

    return new_to_old[head]