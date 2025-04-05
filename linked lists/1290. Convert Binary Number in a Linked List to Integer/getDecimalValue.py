# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        digits = []
        number = 0

        while head:
            digits.append(head.val)
            head = head.next
        
        n = len(digits)
        for i in range(n):
            number += digits[n - 1 - i] * 2**i
        
        return number