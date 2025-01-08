"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root

        # Connect the left child to the right child
        root.left.next = root.right

        # Connect the right child to the left child of the parent's next node
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
        
        return root