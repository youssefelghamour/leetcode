# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = l2_str = ""
        
        # Turn the l1 linked list's value intoa string
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        
        # Turn the l2 linked list's value intoa string
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        
        # Reverse the strings and turn them into unmbers
        num1 = int(l1_str[::-1])
        num2 = int(l2_str[::-1])
        
        # Calculate the total
        total = num1 + num2
        # turn the total into a string and reverse it
        total_str = str(total)[::-1]
        
        # Initialise a linked list with the first value
        head = current = ListNode(int(total_str[0]))
        
        # Create the rest of the nodes
        for i in range(1, len(total_str)):
            # Create new Node and update current to point to it
            current.next = ListNode(int(total_str[i]))
            current = current.next
        
        return head