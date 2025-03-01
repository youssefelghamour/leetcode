# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def intersection(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Finds the intersection of the fast and slow pointer inside the cycle """
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return slow
        
        return None


    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Finds the cycle entrance by moving the slow pointer from the meeting point (where slow and fast met)
            and the start pointer from the head at the same speed
            they meet at the cycle entrance because they both cover the same distance from their positions
        """
        # Pointer from the start of the list
        start = head
        # Pointer from the intersection of fast & slow (last position of slow)
        slow = self.intersection(head)

        if not slow:  # No cycle
            return None
        
        while start != slow:
            # Advance until they meet (at the cycle entrance)
            start = start.next
            slow = slow.next
        
        return start