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

def copyRandomList(head: 'Node') -> 'Node':
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

def main():
    if __name__ == "__main__":
        main()





 