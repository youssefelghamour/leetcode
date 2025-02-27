# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode() # Dummy node
        last_left, last_right = left, right
        curr = head

        while curr:
            if curr.val < x:
                last_left.next = curr
                last_left = last_left.next
            else:
                last_right.next = curr
                last_right = last_right.next
            curr = curr.next
        
        last_right.next = None
        last_left.next = right.next # Skip dummy node
        return left.next