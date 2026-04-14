# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            # Save the next node
            temp = current.next
            # Reverse the current node's pointer
            current.next = prev
            
            # Update prev to current
            prev = current
            # Move to the next node
            current = temp
        
        # New head of the reversed list, since current will be None after the loop
        return prev   