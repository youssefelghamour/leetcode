# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        
        node = head
        while node:
            node = node.next
            length += 1
        
        # Deleting the head node
        if n == length:
            return head.next
                
        node = head
        # Stop before the n'th node to delete
        for i in range(length - 1 - n):
            node = node.next
        
        # Skip the next node
        node.next = node.next.next
        
        return head