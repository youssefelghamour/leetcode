# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        result = []
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        
        sub_len = length // k  # Min length of the sublists
        remainder = length % k  # Number of extra nodes Or the number of sublists that will get an extra node

        curr = head

        for i in range(k):  # K sublists
            result.append(curr) # Add the head of the k'th sublist

            # -1 to get the last node in the sublist so we can set its next to None to split it from the main list
            # +1 if remainder isn't 0 to account for the extra node (We add the remainedr number of extra nodes to the first remainder sublists)
            l = sub_len - 1 + (1 if remainder != 0 else 0)
            for j in range(l):
                if not curr:
                    break
                curr = curr.next

            # Decrease the number of extra nodes since we added one, but stop at 0 so remainder doesn't become negative (for the check above)
            remainder -= (1 if remainder > 0 else 0)

            if curr:
                tmp = curr.next
                # Set the next of the last node in the sublist to None
                curr.next = None
                curr = tmp
        
        return result