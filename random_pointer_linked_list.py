#Creatin a deep comy of a linked list with random pointers
# Writing this code was much easier thanks to the help of github copilot
# I am still trying to figure out how to feed input to main and test the code

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

    new_to_old = {None: None}
    print("old list")
    print_list(head)
    current = head
    while current:
        new_to_old[current] = Node(current.val)
        current = current.next


    current = head

    while current:
        new_to_old[current].next = new_to_old[current.next]
        new_to_old[current].random = new_to_old[current.random]
        current = current.next
    print("new list")
    print_list(new_to_old[head])

    return new_to_old[head]

if __name__ == "__main__":
    main()





 