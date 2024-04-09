# You are given a Singly Linked List of integers. Return true if it has a cycle, else return false.



# A cycle occurs when a node's next points back to a previous node in the list.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Efficiently detects cycles in a linked list using Floyd's Cycle Finding Algorithm.

        Args:
            head: The head node of the linked list.

        Returns:
            True if the linked list has a cycle, False otherwise.
        """

        # Handle empty list or list with only one node
        if not head or not head.next:
            return False

        slow = head
        fast = head

        # Use two pointers, slow and fast. If there's a cycle, fast will eventually catch up to slow.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # Move fast pointer two steps at a time

            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True

        return False

# Example usage
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6  # Create a cycle by connecting node5 to node6

solution = Solution()
has_cycle = solution.hasCycle(node1)
print("Does the linked list have a cycle:", has_cycle)
