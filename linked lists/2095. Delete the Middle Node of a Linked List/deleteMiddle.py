# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        if length == 1:
            return None
        
        mid_index = length // 2
        
        i = 0
        current = head
        # Stop before the middle node
        while i < mid_index - 1:
            current = current.next
            i += 1
        current.next = current.next.next
        
        return head