# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        if curr and curr.next:
            head = curr.next

        while curr and curr.next:
            nxt = curr.next

            curr.next = nxt.next
            nxt.next = curr

            if prev:
                prev.next = nxt

            prev = curr
            curr = curr.next
        
        return head