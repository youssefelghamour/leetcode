# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int

        1. Find the middle of the linked list
            a. Make two pointers one fast (2 nodes) one slow (1 node)
            b. When fast finishes traversing the list, slow will be halfway
        3. Reverse the second half of the linked list by pointing nodes.next to the prev node
        4. Traverse both halfs at the same time and calculate the sums
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # Will point to the end of the linked list
        second_head = middle
        prev = None
        
        # Reverse the second half
        while second_head:
            next_node = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = next_node

        # After the loop second_head will go beyond the last node
        second_head = prev
        
        # print(second_head)
        max_sum = 0
        # First half length = reversed second half length
        while second_head:
            max_sum = max(max_sum, second_head.val + head.val)
            second_head = second_head.next
            head = head.next
        
        return max_sum