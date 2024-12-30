# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The index of the node (starting from 1)
        i = 1
        node = head
        odd = even = None
        head_even = None

        if head:
            # Odd's first node is the head since it's index is 1 (odd)
            odd = head
            # Move the node to point to the next node
            node = head.next
            # Set the counter to even
            i = 2
        if head and head.next:
            # i=2 even's head is the second node
            even = node
            # Save reference of the head of the even linked list
            head_even = even
            node = node.next
            i = 3
        
        
        while node:
            if i % 2 != 0:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
                
            node = node.next
            i += 1
        
        if even:
            # End the even linked list: last node points to None
            even.next = None
        if odd:
            # Link the odd list to the even list
            odd.next = head_even
        
        return head