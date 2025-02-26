# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        l = self.length(head)

        if not head or not head.next:
            return head

        if k > l:
            # ex: rotating 7 times in a 5-item list is like rotating 2 times
            # Since rotating 5 times gives us back the exact list we began with
            # So we just do the leftover rotations after dividing
            k %= l
        
        for i in range(k):
            # Loop to the end (last node doesn't have a next)
            while curr and curr.next:
                prev = curr
                curr = curr.next
            
            prev.next = None
            curr.next = head
            head = curr
        
        return head