# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        
        mid = length // 2
        mid += 1

        for i in range(1, mid):
            head = head.next
        
        return head