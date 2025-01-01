# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvl = 0
        result = []
        current_level = [root]
        
        if not root:
            return []
        
        while current_level:
            current_level_values = []
            next_level = []
            
            for node in current_level:
                current_level_values.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # Reverse current level if the level is odd
            if lvl % 2 != 0:
                current_level_values.reverse()
            
            # Update to the next level
            lvl += 1
            
            result.append(current_level_values)
            current_level = next_level
            
        return result