# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        current_level = [root]
        level = 0
        max_sum = float('-inf')
        max_level = 1

        while current_level:
            level += 1
            next_level = []
            current_level_sum = 0

            for node in current_level:
                current_level_sum += node.val
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if current_level_sum > max_sum:
                max_level = level
                max_sum = current_level_sum
            
            current_level = next_level
            
        return max_level