# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head

        while head and head.val == val:
            head = head.next if head.next else None
            curr = head
        
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next if curr.next.next else None
            else:
                curr = curr.next
        
        return head