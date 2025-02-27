# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Reverses a linked list """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            Reverses the portion of the linked list between positions `left` and `right`

            1. Traverse the list to find the start node at position left and the end node at position right
            2. Isolate the part of the list to reverse by breaking it into three sections: before, middle (start to end), and after
            3. Reverse the middle section
            4. Reconnect the parts: link the node before to the reversed part, and the reversed part to the node after
            5. If left is 1, return the new head, otherwise, return the original head
        """
        # start & end are the nodes of the beg/end of the sub list to be reversed
        start = end = before_list = after_list = reversed_part = None
        current = head
        i = 0

        while current:
            i += 1
            if i == left:  # Found the start node
                start = current
            if i == right: # Found the end node
                end = current
                after_list = end.next  # Node after the end node
                end.next = None  # Break the sublist after end
            if i == left - 1:  # Node just before start
                before_list = current
            current = current.next

        # Reverse the part between start and end
        reversed_part = self.reverseList(start)

        # Connect the reversed part back to the list
        if before_list: # If there is a node before start
            before_list.next = reversed_part
        # start after reversing would become the end node
        start.next = after_list

        # If the reversed part starts at the head, return reversed_part as the new head
        if left == 1:
            return reversed_part
        return head