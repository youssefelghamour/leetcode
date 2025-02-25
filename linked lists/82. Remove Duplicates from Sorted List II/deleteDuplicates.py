# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                tmp = curr
                v = tmp.val

                # While there are duplicates
                while tmp and tmp.val == v:
                    tmp = tmp.next

                if prev:
                    prev.next = tmp
                else:
                    # If there's no previous node, then we are at the beginning
                    head = tmp

                curr = tmp
            else:
                prev = curr
                curr = curr.next
        
        return head