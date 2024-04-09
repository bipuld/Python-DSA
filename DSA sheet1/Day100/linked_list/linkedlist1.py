# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given
# position, 'POS'.
#
# Note :
# Assume that the Indexing for the linked list always starts from 0.
#
# If the position is greater than or equal to the length of the linked list, you should return the same linked list
# without any change.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def delete_node(self, pos):
        """
        Deletes a node at the given position (POS) from the linked list.

        Args:
            pos: The position of the node to be deleted (0-indexed).

        Returns:
            The head of the modified linked list.
        """

        if pos < 0:
            return self  # Return the original list for invalid positions

        temp = self
        count = 0
        prev = None  # Initialize prev to handle head node deletion

        while temp and count < pos:
            prev = temp
            temp = temp.next
            count += 1

        if not temp:  # Position is greater than or equal to the length
            return self  # Return the original list

        if not prev:  # Deleting the head node
            return temp.next  # Update head to point to the next node
        else:
            prev.next = temp.next  # Modify prev.next to skip the deleted node

        return self

a = LinkedList(5)
b = LinkedList(4)
c = LinkedList(3)
d = LinkedList(4)

a.next = b
b.next = c
c.next = d
d.next = None

header = a
while header != None:
    print(header.value, "->")
    header = header.next

print(None)  # Now correctly indented
