# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        result = 0
        current_level = [root]

        while current_level:
            next_level = []

            for node in current_level:
                if low <= node.val <= high:
                    result += node.val
                
                # Optimization: since it's a BST, left < parent < right,
                # so we only need to check left or right if they're in the range
                # if node.val == low, then the whole left subtree < low => out of range
                
                # All values in the left subtree are <= node.val, so they might be still in range
                if node.left and node.val > low:
                    next_level.append(node.left)
                # all values in the right subtree are >= node.val, so they might still be in range
                if node.right and node.val < high:
                    next_level.append(node.right)
            
            current_level = next_level
        
        return result