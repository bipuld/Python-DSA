# ou are given a linked list of N nodes. Your task is to remove the duplicate nodes from the linked list such that every element in the linked list occurs only once i.e. in case an element occurs more than once, only keep its first occurrence in the list.

# For example :
# Assuming the linked list is 3 -> 2 -> 3 -> 4 -> 2 -> 3 -> NULL.

# Number ‘2’ and ‘3’ occurs more than once. Hence we remove the duplicates and keep only their first occurrence. So, our list becomes : 3 -> 2 -> 4 -> NULL.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_duplicates(self, head):
        
        if not head:
            return head
        
        seen = set()
        current = head
        while current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current=current.next
        
        
        
        return head
        
        
        
        
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
node5.next = node6

# Create an instance of the Solution class

head = Solution.remove_duplicates(node1)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next    