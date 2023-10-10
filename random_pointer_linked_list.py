#Creatin a deep comy of a linked list with random pointers
# Writing this code was much easier thanks to the help of github copilot


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def main():     
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    new_to_old = {None: None}

    currernt = head
    while current:
        new_to_old[current] = Node(current.val)
        current = current.next

    current = head

    while current:
        new_to_old[current].next = new_to_old[current.next]
        new_to_old[current].random = new_to_old[current.random]
        current = current.next

    return new_to_old[head]