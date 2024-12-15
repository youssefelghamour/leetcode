# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        values = []
        
        while current:
            values.append(current.val)
            current = current.next
            
        n = len(values)
        for i in range(n//2):
            if values[i] != values[n - 1 -i]:
                return False
        
        return True