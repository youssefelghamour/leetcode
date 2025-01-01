# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse for every current node the left subtree until we reach the left most node
            while current:
                stack.append(current)
                current = current.left
            
            # Previous current is None (left node of most left node)
            # Update the current node to the left most node
            current = stack.pop()
            # Add its value to the result
            result.append(current.val)
            # Process the right subtree of the current node if it exists
            """
                    |
                (current)
                 ___|______
                |          |
              None    (current.right)
            """
            current = current.right
            # If the right subtree is None, the current will be None, and the loop will process the next element from the stack (parent)
                
                
        return result