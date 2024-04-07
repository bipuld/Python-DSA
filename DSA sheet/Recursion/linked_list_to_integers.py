"""
You are given a singly linked list containing ‘n’ nodes, where every node
in the linked list contains a pointer “next” which points to the
next node in the list and having values either 0 or 1.
Your task is to return the decimal representation of the given
number in the linked list.
"""


class LinkedList:

    def __init__(self, values=0, next=None):
        self.next = next
        self.value = values

        # this is instances when Class is called then Automatically it will values =LinkedListNode Value and pointer to
        # next element =next


def binary_to_decimal(head):
    decimal = 0
    current = head
    while current:
        decimal = decimal * 2 + current.value
        current = current.next
    return decimal


head = LinkedList(1)
head.next = LinkedList(0)
head.next.next = LinkedList(1)

result = binary_to_decimal(head)
print("Decimal representation:", result)
