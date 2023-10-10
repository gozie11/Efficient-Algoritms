#Creatin a deep comy of a linked list with random pointers


new_to_old = {}

currernt = head
while current:
    new_to_old[current] = Node(current.val)
    current = current.next

current = head
