# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Convert list A to a list of nodes
        node = headA
        lstA = []
        while node:
            lstA.append(node)
            node = node.next
        
        # Convert list B to a list of nodes
        node = headB
        lstB = []
        while node:
            lstB.append(node)
            node = node.next
            
        lenA, lenB = len(lstA), len(lstB)
        
        # Adjust the lists by skipping the difference in lengths
        diff = abs(lenA - lenB)
        if lenA > lenB:
            # Skip extra nodes at the beginning in A
            lstA = lstA[diff:]
        else:
            # Skip extra nodes at the beginning in B
            lstB = lstB[diff:]
        
        # Compare nodes starting from the first node
        for i in range(min(lenA, lenB)):
            # If the intersection is found
            if lstA[i] == lstB[i]:
                # return the intersection node
                return lstA[i]
        
        return None