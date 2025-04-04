# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
            
        current = root

        while current and (current.right or current.left):  # Ensures current isn't None after the loop
            if val < current.val and current.left:  # Go left
                current = current.left
            elif val > current.val and current.right:  # Go right
                current = current.right
            else:  # If there are no left or right children, break so we can make the new node a child
                break
        
        # Current after the loop will be a leaf: not None, but doesn't have children
        if val < current.val:
            # Make the new node a left child
            current.left = TreeNode(val)
        else:
            # Make the new node a right child
            current.right = TreeNode(val)
        
        return root