# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # Level Order Traversal
        
        if not root:
            return None
        
        current_level = [root]
        
        while current_level:
            next_level = []
            
            for node in current_level:
                if node.val == val:
                    return node
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            current_level = next_level
        
        return None