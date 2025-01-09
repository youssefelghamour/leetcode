# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        stack = []
        current = root
        
        # Find the kth smallest node with the in-order traversal
        # Traverse the tree from the smallest element to the biggest
        while current or stack:
            # Traverse for every current node the left subtree until we reach the left most node
            while current:
                stack.append(current)
                current = current.left
            
            # Previous current is None (left node of most left node)
            # Update the current node to the left most node
            current = stack.pop()
            
            # Increment the counter for every node processed from the stack: how many nodes have been visited in in-order traversal
            counter += 1
            # Stop when we reach the kth smallest node
            if counter == k:
                # Return the kth smalled value
                return current.val

            # Process the right subtree of the current node if it exists
            """
                    ........(parent)...
                    |
                (current)
                 ___|______
                |          |
              None    (current.right)
            """
            current = current.right
            # If the right subtree is None, the current will be None, and the loop will process the next element from the stack (parent)