"""implementation of a linked list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Inserting the Value in the Node
n1 = Node(1)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# now the placing the address of next node in the current node

n1.next = n2  # n1 point the address of the n2
n2.next = n3
n3.next = n4

# insertion at starting node
new_node = Node(50)
new_node.next = n1
head = new_node

# insertion at end
last_node = Node(80)



current = new_node
while current.next is not None:
    current = current.next
current.next = last_node

# deletion from the Starting point
if head.next is None:
    head = head.next

#deletion at end point
current = head
while current.next.next is not None:
    current = current.next
current.next =  None


# deletion from the specific Node
current = head
while current.next.data != 30:
    current = current.next
current.next = current.next.next






current = new_node
while current is not None:
    print(current.data,"->")
    current = current.next
print("None")




